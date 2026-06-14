from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    from pydantic import BaseModel


class BaseTool(ABC):
    name: ClassVar[str]
    description: ClassVar[str]
    args_schema: ClassVar[type[BaseModel] | None] = None

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> str: ...

    def __call__(self, args: dict) -> str:
        return self.run(**args)

    def to_openai_schema(self) -> dict:
        params: dict[str, Any] = {"type": "object", "properties": {}}
        if self.args_schema:
            args_json = self.args_schema.model_json_schema()
            params["properties"] = args_json.get("properties", {})
            if "required" in args_json:
                params["required"] = args_json["required"]
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": params,
            },
        }
