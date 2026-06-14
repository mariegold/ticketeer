from openai import OpenAI


class OpenAIEmbedder:
    """Wraps the OpenAI embeddings API."""

    def __init__(
        self,
        model: str,
        client: OpenAI | None = None,
    ) -> None:
        self.model = model
        self._client = client or OpenAI()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        response = self._client.embeddings.create(model=self.model, input=texts)
        return [item.embedding for item in response.data]

    def embed(self, text: str) -> list[float]:
        return self.embed_batch([text])[0]
