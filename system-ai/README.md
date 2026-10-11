# SYSTEM AI — Phone-first JARVIS prototype

SYSTEM AI is a phone-first personal assistant prototype for Android. The existing Hunter System game at the repository root is unchanged.

## Project files

- `index.html` — mobile dashboard, command interface, 25-minute focus timer, opt-in browser voice controls, and Google search links.
- `app.py` — Flask backend that serves the dashboard locally and exposes `/api/health` and `/api/chat`.
- `requirements.txt` — backend dependency.
- `LOCAL_SETUP.md` — Android/Pydroid setup guide.
- `.env.example` — names of optional server-side environment variables; contains no real secrets.
- `system_ai.py` — original standard-library command-line prototype.

## What works now

### Static GitHub Pages dashboard

Open: https://krishnaamborkar-sys.github.io/hunter-system/system-ai/

- Local dashboard commands and a 25-minute focus timer.
- Browser speech recognition where supported; it starts only when the user taps the microphone button.
- Spoken responses where supported; can be switched off.
- `search: your topic` or `google your topic` creates a Google search link.
- This static page cannot run Python by itself. Chat remains a limited local helper when opened on GitHub Pages.

### Local Python backend on Android

Follow [LOCAL_SETUP.md](LOCAL_SETUP.md). With Flask installed in Pydroid 3, run `app.py` and open `http://127.0.0.1:8765` on the same phone.

- The Python server binds to `127.0.0.1` only.
- The locally served dashboard sends chat messages to `/api/chat`.
- `/api/health` reports the backend mode.
- Messages are not written to a chat-history file.
- Without an AI provider configured, the backend uses a small command helper, **not a generative language model**.
- Google searches open in Google; this project does not scrape search results.

## AI model status

The backend contains an optional adapter for an OpenAI-compatible HTTPS chat-completions endpoint. It is disabled unless `SYSTEM_AI_API_BASE`, `SYSTEM_AI_API_KEY`, and `SYSTEM_AI_MODEL` are provided as server-side environment variables. Do not put real credentials in this repository, in browser JavaScript, or in chat.

This repository does **not** include a bundled generative model, and no AI provider is connected by default. A truly free generative model running entirely on Android depends on compatible model software, device memory, and CPU support; this project does not claim that has already been achieved. Use only services whose terms you are eligible to use. If you have no suitable free provider, keep the optional variables unset.

## Not implemented

- ChatGPT/OpenAI connection or any other live AI provider by default.
- Google search result ingestion; search opens the Google results page.
- Cloud-synced memory or accounts.
- Camera/motion recognition, accessibility service, SMS/contacts access, or unrestricted Android control.
- Background listening. Voice input remains user-triggered.

## Privacy and security

- Never commit API keys, passwords, tokens, or private personal data.
- `.gitignore` excludes local `.env` files and common secret files, but still inspect every commit before pushing.
- If an external AI provider is configured, the user's message is sent to that provider.
- Ask before enabling microphone, camera, accessibility, or background behavior.
- Keep permissions minimal and visible.
- Do not claim an integration is active until it has been connected and tested.

## Existing game

The existing Hunter System game remains in the repository root. SYSTEM AI lives in the `system-ai/` folder so the projects stay separate.
