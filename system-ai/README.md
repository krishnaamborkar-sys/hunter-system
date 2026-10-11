# SYSTEM AI — Hybrid JARVIS Starter

This folder is the first development area for Krishna's phone-first SYSTEM AI project. The existing Hunter System game at the repository root is left unchanged.

## What's included

- `index.html`: mobile-friendly dashboard prototype with a local command interface.
- `system_ai.py`: a standard-library-only Python command-line core.

## Current capabilities

The dashboard and Python script support simple local demo commands: `help`, `study`, `quest`, `profile`, and `status`. The Python core also includes `time`.

## Not connected yet

ChatGPT/OpenAI API, Google/web search, speech recognition, text-to-speech, motion detection, persistent cloud memory, and Android controls are **not connected**. The dashboard labels these clearly rather than pretending they work.

## Open the dashboard

After GitHub Pages publishes the folder, open:

`https://krishnaamborkar-sys.github.io/hunter-system/system-ai/`

If the URL does not load immediately, wait a few minutes for Pages to publish, then reload.

## Run the Python core

On a computer with Python 3, or in an Android Python environment that supports console input:

```bash
python system_ai.py
```

## Planned architecture

1. **Core:** commands, configuration, explicit local preferences.
2. **AI + search:** a small backend service that keeps API secrets server-side; never put secret API keys in browser JavaScript or a public repository.
3. **Voice:** opt-in speech input and spoken responses.
4. **Android bridge:** a dedicated Android app or supported automation integration, with explicit permissions and visible controls.
5. **Motion:** only add motion/session monitoring with clear consent and a visible on/off control.

## Safety and privacy rules

- Never commit API keys, passwords, access tokens, or private user data.
- Ask before enabling microphone, camera, accessibility, or background behavior.
- Prefer the minimum Android permissions needed for each feature.
- Do not claim an integration is active until it has been connected and tested.
