import json
from pathlib import Path


class Config:
    def __init__(self, filename="config.json"):
        self.path = Path(filename)

        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def get(self, key, default=None):
        return self.data.get(key, default)
