# AtomicAds Research Brief Generator

This project implements a **Research Brief Generator** for the AtomicAds AI Engineer assignment.  
It uses **FastAPI**, **LangGraph**, and **structured output generation** concepts to return AI-driven research briefs in JSON format.

---

## ✅ Features Implemented

- **FastAPI Backend** – REST API endpoint `/brief` for generating briefs.
- **LangGraph Pipeline** – Modular state graph design.
- **Mock Mode for Offline Demo** – Works without API keys (ideal for local setup and demo).
- **Pydantic Validation** – Ensures consistent structured responses.
- **CLI Tool** – Generate briefs from the terminal.
- **Testing** – Basic unit tests for API.
- **Docker Support** – Deployment-ready container setup.
- **Documentation** – Sample request & response, architecture overview.

---

## ✅ How It Works

### Workflow:
1. User sends `topic`, `depth`, and `user_id` to `/brief`.
2. The LangGraph pipeline processes the request.
3. A structured JSON response is returned:

```json
{
  "topic": "Edge computing",
  "depth": 2,
  "summary": "This is a mock summary for topic 'Edge computing' with depth 2.",
  "key_findings": ["Finding 1", "Finding 2", "Finding 3"],
  "sources": [
    {"title": "Mock Source 1", "url": "http://example.com", "snippet": "Snippet about the topic."},
    {"title": "Mock Source 2", "url": "http://example.com", "snippet": "Another snippet."}
  ],
  "plan": ["Step 1: Research", "Step 2: Summarize", "Step 3: Validate"],
  "metadata": {"tokens_used": 500},
  "generated_at": "2025-08-13T15:30:00Z"
}
