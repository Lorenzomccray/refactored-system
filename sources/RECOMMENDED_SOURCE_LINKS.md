# RECOMMENDED_SOURCE_LINKS

**Purpose:** Curated external sources to add for project execution. These sources were selected to strengthen the missing runtime layers of `refactored-system` rather than add generic agent noise.

**Use rule:** Add sources in priority order. Prefer official docs, protocol docs, and implementation references over blog posts or product marketing pages.

---

## Priority 1 — Add immediately

### 1. Pydantic
- Docs: https://docs.pydantic.dev/latest/
- Why: typed schemas, validation, fail-closed parsing
- Supports: contracts, task schema, source resolution schema, approval and receipt schemas

### 2. Model Context Protocol (official)
- Docs: https://modelcontextprotocol.io/
- Servers repo: https://github.com/modelcontextprotocol/servers
- Why: clean tool/resource protocol boundaries
- Supports: MCP adapter layer, tool contracts, external capability exposure

### 3. LlamaIndex
- llms.txt: https://developers.llamaindex.ai/llms.txt
- Docs root: https://developers.llamaindex.ai/
- Why: retrieval adapter patterns and document/query orchestration
- Supports: semantic retrieval layer, not core-brain replacement

### 4. Langfuse
- llms.txt: https://langfuse.com/llms.txt
- Docs root: https://langfuse.com/docs
- Why: traces, evals, run comparison, observability
- Supports: receipts, trace store, verification analysis, failure review

### 5. Playwright for Python
- Docs: https://playwright.dev/python/
- Why: browser execution, browser verification, deterministic automation patterns
- Supports: browser plane, environment verification, later delegated producer behavior

### 6. Supabase
- Docs: https://supabase.com/docs
- Why: durable storage, auth, structured state/reference patterns
- Supports: storage adapters, memory/reference persistence, integration references

### 7. n8n
- Docs: https://docs.n8n.io/
- Why: workflow automation patterns without making automation the brain
- Supports: later automation adapter layer

---

## Priority 2 — Add after Phase 1 runtime spine begins landing

### 8. Ollama
- Repo: https://github.com/ollama/ollama
- Docs: https://docs.ollama.com/
- Why: local provider path and private inference option
- Supports: provider plane, local fallback

### 9. vLLM
- Docs: https://docs.vllm.ai/en/latest/
- Repo: https://github.com/vllm-project/vllm
- Why: higher-throughput local inference and serving
- Supports: provider plane, cost/performance routing later

### 10. Qdrant
- Docs: https://qdrant.tech/documentation/
- Repo: https://github.com/qdrant/qdrant
- Why: vector-memory adapter option
- Supports: semantic memory layer, retrieval adapter boundary

### 11. Weaviate
- Docs: https://docs.weaviate.io/
- Repo: https://github.com/weaviate/weaviate
- Why: alternative vector-memory adapter option
- Supports: semantic memory and retrieval experimentation

### 12. Temporal
- Docs: https://docs.temporal.io/
- Repo: https://github.com/temporalio/temporal
- Why: durable workflow and retry/resume patterns
- Supports: later Tasklet-class recurring automation without collapsing runtime law

### 13. OpenTelemetry
- Docs: https://opentelemetry.io/docs/
- Why: portable telemetry, structured tracing, instrumentation standards
- Supports: observability plane, receipts alignment, trace export patterns

---

## Priority 3 — Optional / case-by-case

### 14. FastMCP
- Repo: https://github.com/jlowin/fastmcp
- Why: rapid MCP adapter implementation
- Supports: MCP exposure and tool/resource surfaces

### 15. LangGraph
- Docs: https://langchain-ai.github.io/langgraph/
- Repo: https://github.com/langchain-ai/langgraph
- Why: stateful graph orchestration patterns
- Supports: state machine ideas and optional adapter path
- Warning: do not let it become hidden core control logic

### 16. OpenHands
- Repo: https://github.com/All-Hands-AI/OpenHands
- Why: reference for delegated producer behavior
- Supports: external-controlled execution patterns only

### 17. Aider
- Repo: https://github.com/Aider-AI/aider
- Why: reference for coding-assistant execution loops
- Supports: adapter ideas and coding workflow patterns only

---

## Sources not to prioritize early

Do **not** prioritize these before Phase 1 runtime spine work is real:
- broad agent-framework blogs
- donor repos with weak boundaries
- product marketing pages without implementation detail
- sources focused on UI polish before runtime law
- sources that encourage raw transcript dumping into memory

---

## Best order to add to sources

1. Pydantic
2. MCP official docs + servers repo
3. LlamaIndex
4. Langfuse
5. Playwright
6. Supabase
7. n8n
8. Ollama
9. vLLM
10. Qdrant or Weaviate
11. Temporal
12. OpenTelemetry

---

## Mapping to missing runtime layers

| Missing layer | Best sources |
| :--- | :--- |
| Typed schemas / contracts | Pydantic, OpenAPI/JSON-schema patterns |
| Source routing / context loading | MCP official docs, LlamaIndex |
| Approval and policy | policy docs already canonical; use source additions mainly for adapter constraints and workflow patterns |
| Receipts / traces / observability | Langfuse, OpenTelemetry |
| Browser verification / automation | Playwright |
| Semantic retrieval / memory adapters | LlamaIndex, Qdrant, Weaviate |
| Local provider path | Ollama, vLLM |
| Durable automation | n8n, Temporal |

---

## Final rule

Only add a source if it directly strengthens:
- contracts
- routing
- policy
- receipts / observability
- memory discipline
- adapter boundaries

If it does not help one of those, it is not a priority source for this phase.
