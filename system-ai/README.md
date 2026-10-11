# SYSTEM AI — Hybrid JARVIS Starter

This folder is the first development area for Krishna's phone-first SYSTEM AI project. The existing Hunter System game at the repository root is left unchanged.

## What's included

- `index.html`: mobile-friendly dashboard, local command interface, 25-minute focus timer, and browser speech features where supported.
- `system_ai.py`: a standard-library-only Python command-line core.
- This README: setup notes and an honest status of the integrations.

## Current capabilities

In the dashboard, try `help`, `study`, `quest`, `profile`, `status`, `start timer`, `pause timer`, `reset timer`, or `time`. Use **Speak command** to try speech recognition in a supported browser; it is opt-in and not always listening. Spoken replies depend on browser support and can be turned off.

The Python core separately supports local command-line actions. The browser dashboard and Python script are not connected to each other yet.

## Not connected yet

ChatGPT/OpenAI API, Google/web search, persistent memory, camera-based motion detection, and native Android controls are **not connected**. Browser speech support varies by browser and device. The dashboard labels these limits instead of pretending they work.

## Open the dashboard

After GitHub Pages publishes the folder, open:

`https://krishnaamborkar-sys.github.io/hunter-system/system-ai/`

If it does not load immediately, check **GitHub → repository Settings → Pages** to confirm Pages is enabled for the `main` branch, then wait for the deployment to finish.

## Run the Python core

On a computer with Python 3, or in an Android Python environment that supports console input:

```bash
python system_ai.py
```

## Planned architecture

1. **Core:** commands, configuration, and explicit local preferences.
2. **AI + search:** a backend service that keeps API secrets server-side; never put secret API keys in browser JavaScript or a public repository.
3. **Voice:** opt-in speech input and spoken responses.
4. **Android bridge:** a dedicated Android app or supported automation integration, with explicit permissions and visible controls.
5. **Motion:** add session monitoring only with clear consent and a visible on/off control.

## Safety and privacy rules

- Never commit API keys, passwords, access tokens, or private user data.
- Ask before enabling microphone, camera, accessibility, or background behavior.
- Prefer the minimum Android permissions needed for each feature.
- Do not claim an integration is active until it has been connected and tested.
