import json
import logging
from typing import TYPE_CHECKING

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageFunctionToolCall

from ticketeer.agent.base import BaseAgent

if TYPE_CHECKING:
    from collections.abc import Callable

    from openai.types.chat import ChatCompletionMessageToolCallUnion

    from ticketeer.agent.guardrails import InputGuardrail, OutputGuardrail
    from ticketeer.settings import ChatSettings

logger = logging.getLogger(__name__)


class OpenAIAgent(BaseAgent):
    """BaseAgent implementation using the OpenAI chat completions API."""

    def __init__(
        self,
        settings: ChatSettings,
        client: OpenAI | None = None,
        input_guardrails: list[InputGuardrail] | None = None,
        output_guardrails: list[OutputGuardrail] | None = None,
    ) -> None:
        super().__init__(input_guardrails=input_guardrails, output_guardrails=output_guardrails)
        self._client = client or OpenAI()
        self.model = settings.model
        self.temperature = settings.temperature
        self.tools: list[dict] = []
        self.tool_callables: dict[str, Callable[[dict], str]] = {}

    def invoke(self, messages: list[dict]) -> str:
        input_: list = [{"role": "system", "content": self.system_prompt}, *messages]
        input_ = self._apply_input_guardrails(input_)

        while True:
            kwargs: dict = {"model": self.model, "messages": input_, "temperature": self.temperature}
            if self.tools:
                kwargs["tools"] = self.tools
                kwargs["tool_choice"] = "auto"

            response = self._client.chat.completions.create(**kwargs)
            message = response.choices[0].message
            # append the full message object (not just content) — the API requires the
            # assistant turn with its tool_calls field present in history for the next request
            input_.append(message)

            if not message.tool_calls:
                # content can be None when the model's last action was a tool call
                return self._apply_output_guardrails(message.content or "")

            for tool_call in message.tool_calls:
                result = self._dispatch(tool_call)
                input_.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )

    def _dispatch(self, tool_call: ChatCompletionMessageToolCallUnion) -> str:
        if isinstance(tool_call, ChatCompletionMessageFunctionToolCall):
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            fn = self.tool_callables.get(name)
            if fn is None:
                return f"Unknown tool: {name}"
            try:
                logger.info("Calling tool %s", name)
                return str(fn(args))
            except Exception as exc:  # noqa: BLE001
                # return the error as a string so the model can see it and potentially retry
                return f"Tool '{name}' raised an error: {exc}"
        else:
            return f"Unknown tool: {tool_call.model_dump()}"
