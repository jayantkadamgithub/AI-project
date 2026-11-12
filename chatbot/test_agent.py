import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from agent import ChatbotAgent


def test_chat_returns_response():
    agent = ChatbotAgent(system_prompt="You are a test assistant.")
    response = agent.chat("Say 'hello test' and nothing else.")
    assert isinstance(response, str) and len(response) > 0
    print("PASS: chat returned a response")


def test_clear_history():
    agent = ChatbotAgent()
    agent.chat("remember this")
    agent.clear_history()
    history = agent.get_history()
    assert len(history) == 1
    assert history[0]["role"] == "system"
    print("PASS: clear_history resets to system message only")


if __name__ == "__main__":
    test_chat_returns_response()
    test_clear_history()
