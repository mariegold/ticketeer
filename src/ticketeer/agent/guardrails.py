class BaseGuardrail:
    def apply(self, content: str) -> str:
        return content


class InputGuardrail(BaseGuardrail):
    """Placeholder base for e.g. PII detection, topic restriction, prompt injection detection."""


class OutputGuardrail(BaseGuardrail):
    """Placeholder base for e.g. hallucination detection, citation checking, toxicity filter."""
