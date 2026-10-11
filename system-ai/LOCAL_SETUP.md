# Run SYSTEM AI locally on Android

This runs the Python backend on the same phone and serves the dashboard from the backend. It does not give SYSTEM unrestricted phone access.

## 1. Install the dependency

1. Open Pydroid 3.
2. Open Pip/package installer.
3. Install `flask`.
4. Return to the editor.

## 2. Get the project files

Download or clone the repository files so that `app.py` and `index.html` are in the same `system-ai` folder. In Pydroid, open `app.py` from that folder.

## 3. Start the server

Run `app.py`. The console should show:

```
SYSTEM AI backend ready: http://127.0.0.1:8765
```

While the script is running, open Chrome on the same phone and visit:

`http://127.0.0.1:8765`

The backend binds only to `127.0.0.1`, so it is not exposed to other devices on Wi-Fi. Keep Pydroid running while using the local dashboard. If port 8765 is busy, set `SYSTEM_AI_PORT` before launching or change the default in `app.py`.

## 4. Test the API

Open `http://127.0.0.1:8765/api/health` in the same phone browser. A successful response includes `"ok": true`.

In the dashboard, type `status`, then `study`. The local helper works without any API key. It is not a generative LLM and will not invent an answer for arbitrary questions.

## AI provider configuration

The backend has optional support for an OpenAI-compatible chat-completions endpoint using these server-side environment variables:

- `SYSTEM_AI_API_BASE` (must be HTTPS)
- `SYSTEM_AI_API_KEY`
- `SYSTEM_AI_MODEL`

These values are read only by Python; they are never sent to browser JavaScript. Do not commit real values to GitHub or paste them into ChatGPT. Use only a provider whose terms you are eligible to use. If you have no suitable free provider, leave these variables unset; local helper mode still works.

Do not put secrets in `.env.example`. If you create a private local `.env`, keep it ignored by Git and load it only in your own environment. This starter does not automatically load dotenv files.

## Hosted GitHub Pages

GitHub Pages serves static files only; it cannot run `app.py`. Use `https://krishnaamborkar-sys.github.io/hunter-system/system-ai/` for the static demo. Use `http://127.0.0.1:8765` when running the local Python backend on your phone.

## Privacy and safety

- The server listens on loopback only.
- No chat history is written to disk.
- Do not add camera, microphone, accessibility, SMS, contacts, or background permissions without a clear need and an explicit on/off control.
- If an external AI provider is configured, message text is sent to that provider. Do not send passwords, API keys, private documents, or sensitive personal information.
