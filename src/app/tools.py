tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Возвращает текущую дату, день недели и точное время на ПК.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "open_youtube",
            "description": "Открывает сайт YouTube в браузере.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "sleep_system",
            "description": "Переводит ПК в спящий режим.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "open_telegram",
            "description": "Открывает программу Telegram desktop (месенджер).",
            "parameters": {"type": "object", "properties": {}},
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_steam",
            "description": "Открывает программу Steam (лаунчер игр).",
            "parameters": {"type": "object", "properties": {}},
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_music",
            "description": "Открывает программу MusicBee (музыкальный плеер). Запускать, если пользователь хочет послушать музыку.",
            "parameters": {"type": "object", "properties": {}},
        }
    }
]
