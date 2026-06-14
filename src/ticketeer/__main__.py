import logging

from openai import OpenAI

from ticketeer.agent.it_support import ITSupportAgent
from ticketeer.agent.prompts import Prompts
from ticketeer.knowledge_base.chunking import SlidingWindowChunker
from ticketeer.knowledge_base.embedding import OpenAIEmbedder
from ticketeer.knowledge_base.service import KnowledgeBaseService
from ticketeer.settings import ServiceSettings
from ticketeer.tickets.sql_database import SQLiteDatabase

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def main() -> None:
    settings = ServiceSettings()
    client = OpenAI(api_key=settings.openai_api_key)

    # Initialize the structured database
    db = SQLiteDatabase(db_path=settings.db_path)

    # Initialize knowledge base for unstructured data
    chunker = SlidingWindowChunker()
    embedder = OpenAIEmbedder(model=settings.embedding_model, client=client)
    knowledge_base = KnowledgeBaseService(
        chunker=chunker,
        embedder=embedder,
        path=settings.knowledge_base_path,
        settings=settings,
    )

    # Initialize agent
    agent = ITSupportAgent(
        settings=settings,
        client=client,
        knowledge_base=knowledge_base,
        db=db,
        prompts=Prompts(),
    )

    history: list[dict] = []

    print("Hi there, I am your IT support assistant. Ask me a question or type 'exit' to quit.")

    while True:
        try:
            question = input("You: ").strip()
        except EOFError, KeyboardInterrupt:
            break
        if not question or question.lower() in ("exit", "quit"):
            break

        history.append({"role": "user", "content": question})
        answer = agent.invoke(history)

        print(f"\nAssistant: {answer}\n")
        history.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
