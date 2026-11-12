import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ChatbotAgent:
    def __init__(self, model: str | None = None, system_prompt: str | None = None):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-key-here":
            raise ValueError(
                "OPENAI_API_KEY not set. Copy .env.example to .env and add your key."
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.system_prompt = system_prompt or (
            "You are a helpful, concise chatbot assistant. "
            "Answer the user's questions clearly and accurately."
        )
        self.history: list[dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
        )
        assistant_msg = response.choices[0].message.content or ""
        self.history.append({"role": "assistant", "content": assistant_msg})
        return assistant_msg

    def clear_history(self) -> None:
        self.history = [{"role": "system", "content": self.system_prompt}]

    def get_history(self) -> list[dict[str, str]]:
        return list(self.history)
