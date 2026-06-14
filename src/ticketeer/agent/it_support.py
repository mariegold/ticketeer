from typing import TYPE_CHECKING

from ticketeer.agent.openai import OpenAIAgent
from ticketeer.agent.prompts import PromptId, Prompts
from ticketeer.agent.tools.knowledge_base_tool import SearchKnowledgeBaseTool
from ticketeer.agent.tools.sql_tools import DiscoverSchemaTool, ExecuteSQLTool, SampleDataTool

if TYPE_CHECKING:
    from openai import OpenAI

    from ticketeer.knowledge_base.service import KnowledgeBaseService
    from ticketeer.settings import ChatSettings
    from ticketeer.tickets.base import BaseDatabase


class ITSupportAgent(OpenAIAgent):
    def __init__(
        self,
        settings: ChatSettings,
        prompts: Prompts,
        knowledge_base: KnowledgeBaseService,
        db: BaseDatabase,
        client: OpenAI | None = None,
    ) -> None:
        super().__init__(settings=settings, client=client)
        self.system_prompt = prompts.get_prompt(PromptId.SYSTEM)
        tools = [
            SearchKnowledgeBaseTool(knowledge_base),
            ExecuteSQLTool(db),
            DiscoverSchemaTool(db),
            SampleDataTool(db),
        ]
        self.tools = [t.to_openai_schema() for t in tools]
        self.tool_callables = {t.name: t for t in tools}
