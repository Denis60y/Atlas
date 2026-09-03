from ollama import Client
from app.functions import available_functions
from app.tools import tools_schema

from core.utils.config import mainConfig


client = Client(host="http://localhost:11434", trust_env=False)


def warmup_model(model_name: str) -> None:
    """Отправляет тестовый запрос для загрузки модели в память до начала работы."""
    print("Загрузка и инициализация модели...", end="", flush=True)
    try:
        client.chat(
            model=model_name,
            messages=[{"role": "user", "content": "ping"}],
        )
        print("\rМодель готова к работе!             ")
    except Exception as e:
        print(f"\nОшибка при инициализации модели: {e}")


def start() -> None:
    model_name = mainConfig.get("model_name")

    warmup_model(model_name)

    messages = []

    while True:
        try:
            user_input = input("\n> ")
        except (KeyboardInterrupt, EOFError):
            break

        if not user_input.strip():
            continue

        messages.append({"role": "user", "content": user_input})

        response = client.chat(
            model=model_name,
            messages=messages,
            tools=tools_schema,
        )

        message = response["message"]

        if message.get("tool_calls"):
            messages.append(message)

            for tool in message["tool_calls"]:
                func_name = tool["function"]["name"]

                if func_name in available_functions:
                    result = available_functions[func_name]()

                    messages.append(
                        {
                            "role": "tool",
                            "content": str(result),
                        }
                    )

            final_response = client.chat(model=model_name, messages=messages)

            print(final_response["message"]["content"])
            messages.append(final_response["message"])
        else:
            print(message["content"])
            messages.append(message)


if __name__ == "__main__":
    start()
