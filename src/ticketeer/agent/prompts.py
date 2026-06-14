from enum import StrEnum
from pathlib import Path

import yaml


class PromptId(StrEnum):
    SYSTEM = "system"


class Prompts:
    """Loads prompts.yaml once at init."""

    def __init__(self, file: str = "prompts.yaml") -> None:
        self.file = Path(__file__).parent / file
        with self.file.open() as fp:
            self._data = yaml.safe_load(fp.read())

    def get_prompt(self, prompt_id: PromptId) -> str:
        return self._data[prompt_id.value]
