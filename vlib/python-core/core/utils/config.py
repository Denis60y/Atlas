import json
from pathlib import Path


class Config:
    _tag = "config"

    BASE_DIR = Path(__file__).resolve().parents[4]
    _config_path = BASE_DIR / "config.json"

    def get(self, field: str) -> str:
        if not self._config_path.exists():
            raise FileNotFoundError(f"Файл не найден по пути: {self._config_path}")

        with open(self._config_path, "r", encoding="utf-8") as f:
            return json.load(f)[field]


mainConfig = Config()
