# ticketeer

A CLI chatbot for an internal IT helpdesk. Ask a question in natural language and get an answer grounded in two data sources: a history of past support tickets (SQLite) and a knowledge base of runbooks, FAQs, and policy documents (Markdown).

Built with the OpenAI SDK.

---

## Setup

**Requirements:** Python ≥ 3.14, `uv` for dependency management, and an OpenAI API key.

```bash
uv sync                                                                                                                                                                                                                                                                                                                   
source .venv/bin/activate                                                                                                                                                                                                                                                                                                 

export OPENAI_API_KEY=sk-...
poe start  # or python -m ticketeer
```

Type a question at the prompt. Type `exit` or `quit` (or send EOF) to stop.

---

## Data

### Ticket database

200 synthetic support tickets in a SQLite database, covering six categories (`access`, `hardware`, `software`, `network`, `account`, `security`) and three statuses (`resolved`, `open`, `escalated`). Generated with a fixed seed — deterministic and idempotent. See [`data/TICKETS.md`](data/TICKETS.md) for details.

To regenerate:

```bash
poe generate-data
```

### Knowledge base

See [`data/KNOWLEDGE_BASE.md`](data/KNOWLEDGE_BASE.md) for details. The vector index is cached to `data/md/knowledge_base.json` and rebuilt automatically if deleted.

---

## Configuration

All settings can be overridden with environment variables:

| Variable | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | _(required)_ | OpenAI API key |
| `MODEL` | `gpt-4o-mini` | Chat model |
| `TEMPERATURE` | `0.1` | Sampling temperature |
| `EMBEDDING_MODEL` | `text-embedding-3-small` | Embedding model for the vector index |
| `TOP_K` | `3` | Number of knowledge base chunks to retrieve |
| `SIMILARITY_THRESHOLD` | `0.3` | Minimum cosine similarity for a chunk to be returned |
| `DATA_DIR` | `data/` | Root directory for the database and knowledge base |

---

## Project structure

```
data/
  sqlite/tickets.db           # ticket database
  md/                         # knowledge base articles (faq/, policy/, runbooks/)
  md/knowledge_base.json      # cached vector index (auto-generated)

scripts/ticket_generation/    # synthetic ticket generator

src/ticketeer/
  agent/                      # tool-use loop, prompt loading, guardrail hooks
  agent/tools/                # SQL tools, knowledge base search tool
  tickets/                    # SQLite access and ticket service layer
  knowledge_base/             # chunking, embedding, vector store, KB service
```

---

## How it works

The agent maintains a conversation history and runs a tool-use loop on every turn: it calls the OpenAI chat completions API, dispatches whichever tools the model requests, feeds the results back, and repeats until the model produces a final text response.

To answer questions about previous tickets, the agent first inspects the schema and a sample of rows to orient itself, then generates a SQL query and executes it. If the query fails, the error is fed back and the model retries. Results come back as JSON and are summarised in the response.

The agent may also run a semantic search over the knowledge base. The articles are chunked, embedded, and the vector index is saved to disk. Subsequent runs load from the cache. The top matching passages are retrieved by cosine similarity and passed as context to the model.

Both paths can be combined in a single turn — the agent calls whichever tools are relevant and synthesises one answer.


---

## Development

```bash
poe fmt          # format
poe lint         # lint
poe type-check   # type check
pytest           # run tests
```

Tools: [ruff](https://docs.astral.sh/ruff/), [ty](https://github.com/astral-sh/ty), [pytest](https://pytest.org) + [pytest-mock](https://pytest-mock.readthedocs.io/), [poethepoet](https://poethepoet.natn.io/).
