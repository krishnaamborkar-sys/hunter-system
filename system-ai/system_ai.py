"""SYSTEM AI starter core — safe local command router.

Run with: python system_ai.py
This module intentionally does not access the network, microphone, camera,
or phone controls. Those integrations belong in later, permission-aware phases.
"""
from datetime import datetime


def system_status() -> str:
    return (
        "SYSTEM AI status\n"
        "Python core: online\n"
        "AI API: not connected\n"
        "Web search: not connected\n"
        "Voice: not connected\n"
        "Android controls: not connected"
    )


def handle_command(command: str) -> str:
    cmd = command.strip().lower()
    if not cmd:
        return "Type a command. Try 'help'."
    if cmd in {"help", "commands"}:
        return (
            "Commands: help, study, quest, profile, status, time, exit\n"
            "This is the first local prototype; integrations are not connected yet."
        )
    if cmd in {"study", "start study"}:
        return (
            "Scholar Core ready. Choose one JEE topic, study for 25 minutes, "
            "solve 3 questions, then review every mistake."
        )
    if cmd in {"quest", "daily quest"}:
        return (
            "Daily Quest (demo):\n"
            "1. Complete one focused JEE session.\n"
            "2. Review mistakes and write one takeaway.\n"
            "3. Take a short movement and water break.\n"
            "Quest completion tracking will be added later."
        )
    if cmd == "profile":
        return (
            "Hunter: Krishna\n"
            "Mission: JEE preparation + consistent training\n"
            "Persistent profile sync: not connected"
        )
    if cmd == "status":
        return system_status()
    if cmd == "time":
        return "Local device time: " + datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    return (
        "I am in local demo mode. Try 'help', 'study', 'quest', 'profile', "
        "'status', or 'time'. AI chat and web search will require a secure backend."
    )


def main() -> None:
    print("SYSTEM AI — Local Core")
    print("Type 'help' for commands, or 'exit' to quit.\n")
    while True:
        try:
            command = input("You > ")
        except (EOFError, KeyboardInterrupt):
            print("\nSYSTEM > Session ended.")
            break
        if command.strip().lower() in {"exit", "quit", "bye"}:
            print("SYSTEM > Session ended. Rest well, Hunter.")
            break
        print("SYSTEM > " + handle_command(command) + "\n")


if __name__ == "__main__":
    main()
