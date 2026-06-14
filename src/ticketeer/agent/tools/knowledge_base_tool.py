import logging
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from ticketeer.agent.tools.base import BaseTool

if TYPE_CHECKING:
    from ticketeer.knowledge_base.service import KnowledgeBaseService

logger = logging.getLogger(__name__)


class SearchKnowledgeBaseArgs(BaseModel):
    query: str = Field(description="Natural language search query.")


class SearchKnowledgeBaseTool(BaseTool):
    name = "search_knowledge_base"
    description = (
        "Search the IT knowledge base (runbooks, FAQs, policy docs)"
        " for how-to questions, policy lookups, and procedures."
    )
    args_schema = SearchKnowledgeBaseArgs

    def __init__(self, knowledge_base: KnowledgeBaseService) -> None:
        self._knowledge_base = knowledge_base

    def run(self, query: str) -> str:
        chunks = self._knowledge_base.search(query)
        results = self._knowledge_base.format_results(chunks)
        logger.debug("Search results from knowledge base: %s", results)
        return results
