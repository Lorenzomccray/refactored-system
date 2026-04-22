# REMOTE DOC SURFACES

## Purpose

List machine-friendly external documentation surfaces that the assistant should prefer when vendor or protocol details matter.

## Preferred formats
1. `llms-full.txt`
2. `llms.txt`
3. docs MCP servers
4. markdown
5. JSON or schema endpoints
6. structured HTML

## Surfaces

### OpenAI Developer Docs MCP
- URL: `https://developers.openai.com/mcp`
- Type: public docs MCP server
- Scope: OpenAI developer documentation only
- Notes: read-only documentation surface

### MCP official docs
- URL: `https://modelcontextprotocol.io/llms-full.txt`
- Type: protocol docs index
- Scope: architecture, protocol, registry, SDK concepts
- Notes: use for official protocol behavior and publishing rules

### Langfuse docs MCP
- URL: `https://langfuse.com/api/mcp`
- Type: public docs MCP server
- Scope: Langfuse docs search + page retrieval
- Notes: no auth required for docs surface

### Langfuse llms.txt
- URL: `https://langfuse.com/llms.txt`
- Type: llms index
- Scope: Langfuse documentation overview

### LlamaIndex docs
- URLs:
  - `https://developers.llamaindex.ai/llms.txt`
  - `https://developers.llamaindex.ai/api/search?q=&limit=10&full-content=true`
  - `https://developers.llamaindex.ai/api/read?path=/python/framework/&startLine=0&endLine=500`
- Type: llms + JSON doc APIs
- Scope: retrieval, RAG, workflows, integrations

### Pydantic AI MCP docs
- URL: `https://pydantic.dev/docs/ai/mcp/overview/`
- Type: official docs page
- Scope: MCP client/server usage and durable execution tie-ins

## Use rules
- Prefer official surfaces over blog posts.
- Use remote docs only when internal doctrine is silent or when freshness matters.
- If external docs imply a change to internal doctrine, record the variance before adopting it.
