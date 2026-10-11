"""SYSTEM AI local backend.

Runs on the user's Android phone with Pydroid 3 + Flask.
No API key is required. By default it uses transparent local helper responses.
An optional OpenAI-compatible provider can be configured via environment variables;
secrets must never be stored in this repository or browser code.
"""
from __future__ import annotations

import json
import os
import re
import socket
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote_plus

from flask import Flask, jsonify, request, send_file

ROOT = Path(__file__).resolve().parent
INDEX_FILE = ROOT / "index.html"
HOST = "127.0.0.1"
PORT = int(os.environ.get("SYSTEM_AI_PORT", "8765"))
MAX_MESSAGE_CHARS = 2000
AI_BASE_URL = os.environ.get("SYSTEM_AI_API_BASE", "").strip().rstrip("/")
AI_API_KEY = os.environ.get("SYSTEM_AI_API_KEY", "").strip()
AI_MODEL = os.environ.get("SYSTEM_AI_MODEL", "").strip()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


def local_reply(message: str) -> str:
    """Honest offline command helper; this is not a generative LLM."""
    text = message.strip()
    low = text.lower()
    if not text:
        return "Type a question or command."
    if low in {"help", "commands"}:
        return ("SYSTEM local commands: study, quest, profile, status, time, "
                "start timer, pause timer, reset timer, and search: your topic. "
                "This local mode does not yet run a generative language model.")
    if low == "status":
        configured = bool(AI_BASE_URL and AI_API_KEY and AI_MODEL)
        return ("Python backend is online. Mode: " +
                ("configured AI provider" if configured else "local helper (no AI model configured)") +
                ". No phone controls are enabled.")
    if low == "study" or "start study" in low:
        return ("JEE Scholar plan: choose one small subtopic, work for 25 minutes, "
                "solve 3 questions without checking solutions, then log each mistake "
                "as concept, calculation, rush, or guessing. Use the dashboard timer.")
    if low == "quest" or "daily quest" in low:
        return ("Study quest: (1) one focused study block, (2) solve practice questions, "
                "(3) review mistakes, (4) take a water and movement break. "
                "This demo does not persist completion.")
    if low == "profile":
        return ("Hunter profile: Krishna. Mission: JEE preparation and consistent, "
                "balanced training. Profile data is not synced or saved by this backend.")
    if low == "time":
        from datetime import datetime
        return "Phone/server time: " + datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    if low.startswith("search:") or low.startswith("google "):
        query = re.sub(r"^(search:|google)\s*", "", text, flags=re.I).strip()
        if not query:
            return "Add a topic, for example: search: JEE rotational motion."
        return "SEARCH_URL:" + "https://www.google.com/search?q=" + quote_plus(query)
    return ("I'm receiving your message through the Python backend, but the local helper "
            "is not a generative AI model yet. Try 'study', 'quest', 'status', or "
            "'search: your topic'. To enable natural AI answers, configure a compatible "
            "provider on the server only; never paste keys into GitHub or this chat.")


def call_optional_ai(message: str) -> str | None:
    """Optional OpenAI-compatible chat endpoint. Disabled unless all env values exist."""
    if not (AI_BASE_URL and AI_API_KEY and AI_MODEL):
        return None
    # Only allow HTTPS so a configured API key is not sent over plain HTTP.
    if not AI_BASE_URL.lower().startswith("https://"):
        app.logger.warning("AI provider disabled: SYSTEM_AI_API_BASE must use HTTPS.")
        return None
    url = AI_BASE_URL + "/chat/completions"
    body = json.dumps({
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": (
                "You are SYSTEM, a helpful study assistant. Be clear and concise. "
                "For JEE, explain step by step. Do not claim access to the user's phone, "
                "files, camera, or accounts. Do not request secrets."
            )},
            {"role": "user", "content": message[:MAX_MESSAGE_CHARS]},
        ],
        "temperature": 0.5,
    }).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + AI_API_KEY},
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            payload = json.loads(response.read(1_000_000).decode("utf-8"))
        answer = payload["choices"][0]["message"]["content"]
        if isinstance(answer, str) and answer.strip():
            return answer.strip()[:8000]
    except (urllib.error.URLError, TimeoutError, KeyError, IndexError, ValueError, OSError) as exc:
        app.logger.warning("AI request failed (%s). Falling back to local helper.", type(exc).__name__)
    return None


@app.get("/")
def dashboard():
    if not INDEX_FILE.is_file():
        return "SYSTEM AI dashboard file index.html is missing.", 500
    return send_file(INDEX_FILE)


@app.get("/api/health")
def health():
    configured = bool(AI_BASE_URL and AI_API_KEY and AI_MODEL and AI_BASE_URL.lower().startswith("https://"))
    return jsonify({
        "ok": True,
        "service": "SYSTEM AI local backend",
        "mode": "configured-ai" if configured else "local-helper",
        "ai_model_configured": configured,
        "secrets_in_browser": False,
    })


@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    if not isinstance(message, str):
        return jsonify({"error": "message must be text"}), 400
    message = message.strip()
    if not message:
        return jsonify({"error": "message cannot be empty"}), 400
    if len(message) > MAX_MESSAGE_CHARS:
        return jsonify({"error": f"message limit is {MAX_MESSAGE_CHARS} characters"}), 413
    answer = call_optional_ai(message) or local_reply(message)
    if answer.startswith("SEARCH_URL:"):
        return jsonify({"reply": "Open the search link below.", "search_url": answer.split(":", 1)[1]})
    return jsonify({"reply": answer})


@app.get("/api/search")
def search():
    query = request.args.get("q", "").strip()[:300]
    if not query:
        return jsonify({"error": "Provide a search query using ?q=..."}), 400
    return jsonify({
        "query": query,
        "url": "https://www.google.com/search?q=" + quote_plus(query),
        "note": "Search opens in Google; results are not scraped or stored by SYSTEM AI.",
    })


def main() -> None:
    # Bind to loopback only. Other devices on Wi-Fi cannot connect to this server.
    with socket.socket() as sock:
        sock.bind((HOST, PORT))
    print(f"SYSTEM AI backend ready: http://{HOST}:{PORT}")
    print("Open that URL in Chrome on this phone. Stop the server with Ctrl+C / the Pydroid stop control.")
    print("Mode: " + ("optional AI configured" if AI_BASE_URL and AI_API_KEY and AI_MODEL else "local helper; no AI model configured"))
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
