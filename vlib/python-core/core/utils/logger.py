import datetime
from dataclasses import dataclass
from enum import Enum


class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'


@dataclass
class _LogLevel:
    name: str
    priority: int


class Level(Enum):
    Fatal = _LogLevel("F", 7)
    Error = _LogLevel("E", 6)
    Warning = _LogLevel("W", 5)
    Info = _LogLevel("I", 4)
    Debug = _LogLevel("D", 3)
    Profile = _LogLevel("P", 2)
    Verbose = _LogLevel("V", 1)


level_info = {
    Level.Fatal: (Colors.RED, "F"),
    Level.Error: (Colors.MAGENTA, "E"),
    Level.Warning: (Colors.YELLOW, "W"),
    Level.Info: (Colors.CYAN, "I"),
    Level.Debug: (Colors.BLUE, "D"),
    Level.Profile: (Colors.GREEN, "P"),
    Level.Verbose: (Colors.WHITE, "V"),
}


class Logger:
    _tag = "logger"

    _color: Colors = None

    def f(self, tag: str, message: str) -> None:
        self.write(Level.Fatal, tag, message)

    def e(self, tag: str, message: str) -> None:
        self.write(Level.Error, tag, message)

    def w(self, tag: str, message: str) -> None:
        self.write(Level.Warning, tag, message)

    def i(self, tag: str, message: str) -> None:
        self.write(Level.Info, tag, message)

    def d(self, tag: str, message: str) -> None:
        self.write(Level.Debug, tag, message)

    def p(self, tag: str, message: str) -> None:
        self.write(Level.Profile, tag, message)

    def v(self, tag: str, message: str) -> None:
        self.write(Level.Verbose, tag, message)

    def write(self, level: Level, tag: str, message: str) -> None:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self._write(level, now, tag, message)

    def _write(self, level: Level, time: str, tag: str, message: str) -> None:
        color, letter = level_info[level]
        mes = f"{color}[{time}] [{letter}] [{tag}]: {message}{color}"
        print(mes)


Log = Logger()
