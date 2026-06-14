from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ticketeer.agent.guardrails import InputGuardrail, OutputGuardrail


class BaseAgent:
    """Provider-agnostic agent interface."""

    def __init__(
        self,
        input_guardrails: list[InputGuardrail] | None = None,
        output_guardrails: list[OutputGuardrail] | None = None,
    ) -> None:
        self.system_prompt: str = ""
        self.input_guardrails: list[InputGuardrail] = input_guardrails or []
        self.output_guardrails: list[OutputGuardrail] = output_guardrails or []

    def invoke(self, messages: list[dict]) -> str:
        raise NotImplementedError

    def _apply_input_guardrails(self, messages: list) -> list:
        if not self.input_guardrails:
            return messages
        last = messages[-1]
        if last.get("role") == "user" and isinstance(last.get("content"), str):
            content = last["content"]
            for g in self.input_guardrails:
                content = g.apply(content)
            messages = [*messages[:-1], {**last, "content": content}]
        return messages

    def _apply_output_guardrails(self, text: str) -> str:
        for g in self.output_guardrails:
            text = g.apply(text)
        return text
