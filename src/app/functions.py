import os
from datetime import datetime
import subprocess
import webbrowser


def open_telegram() -> str:
    """Открывает программу Telegram."""
    try:
        os.startfile("Telegram.exe")
        return "Telegram успешно открыт."
    except Exception as e:
        return f"Ошибка: {e}"


def open_music() -> str:
    """Открывает программу MusicBee."""
    try:
        os.startfile("MusicBee.exe")
        return "MusicBee успешно открыт."
    except Exception as e:
        return f"Ошибка: {e}"


def open_steam() -> str:
    """Открывает программу Steam."""
    try:
        os.startfile("steam.exe")
        return "Steam успешно открыт."
    except Exception as e:
        return f"Ошибка: {e}"


def open_youtube() -> str:
    """Открывает главную страницу YouTube в браузере по умолчанию."""
    webbrowser.open("https://www.youtube.com")
    return "YouTube успешно открыт"


def sleep_system() -> str:
    """Отправляет ноутбук в спящий режим."""
    subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"])
    return "Система переведена в спящий режим"


def get_current_time() -> str:
    """Возвращает текущую дату, день недели и точное время."""
    now = datetime.now()
    return now.strftime("Сегодня %A, %d.%m.%Y, точное время: %H:%M:%S") 


available_functions = {
    "get_current_time": get_current_time,
    "open_youtube": open_youtube,
    "sleep_system": sleep_system,
    "open_telegram": open_telegram,
    "open_steam": open_steam,
    "open_music": open_music,
}