from agent import ChatbotAgent


def print_help() -> None:
    print("Commands: /quit, /clear, /history, /help")


def main() -> None:
    try:
        agent = ChatbotAgent()
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print("Chatbot Agent — type /quit to exit")
    print_help()

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input == "/quit":
            print("Goodbye!")
            break

        if user_input == "/clear":
            agent.clear_history()
            print("History cleared.")
            continue

        if user_input == "/history":
            for msg in agent.get_history():
                role = msg["role"].upper()
                print(f"[{role}] {msg['content']}")
            continue

        if user_input == "/help":
            print_help()
            continue

        try:
            response = agent.chat(user_input)
            print(f"\nAgent: {response}")
        except Exception as exc:
            print(f"\nError: {exc}")


if __name__ == "__main__":
    main()
