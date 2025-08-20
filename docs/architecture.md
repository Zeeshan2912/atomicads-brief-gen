# AtomicAds – Design & Execution Documentation

---

## 1. Problem Statement and Objective

Modern marketers and businesses need to generate concise, targeted advertising briefs quickly and efficiently. Manual brief creation is time-consuming and often inconsistent. AtomicAds leverages Generative AI to automate this process, providing high-quality, structured briefs via both API and CLI, with full traceability and modularity.

---

## 2. System Architecture

### 2.1 High-Level Overview

AtomicAds is built on a modular, layered architecture:

- **API Layer:** FastAPI for RESTful endpoints.
- **CLI Layer:** Command-line interface for local usage.
- **Orchestration Layer:** LangChain graph for workflow management.
- **LLM Layer:** OpenAI/Groq models for text generation.
- **Retrieval Layer:** Search and context gathering.
- **Persistence Layer:** SQLite for checkpointing and traceability.
- **Tracing Layer:** LangSmith for observability.

### 2.2 Visual Representation

```
+-------------------+
|    User Input     |
+-------------------+
			|
			v
+-------------------+      +-------------------+
|   API (FastAPI)   |<---->|   CLI Interface   |
+-------------------+      +-------------------+
			|
			v
+-------------------+
|  Orchestration    |  (LangChain Graph)
+-------------------+
			|
			v
+-------------------+
|   LLM (OpenAI)    |
+-------------------+
			|
			v
+-------------------+
|   Validation      |  (Pydantic Schemas)
+-------------------+
			|
			v
+-------------------+
|   Persistence     |  (SQLite)
+-------------------+
			|
			v
+-------------------+
|   Tracing         |  (LangSmith)
+-------------------+
```

---

## 3. Model and Tool Selection Rationale

- **LLMs (OpenAI/Groq):** Chosen for their state-of-the-art language generation and flexibility.
- **LangChain:** Enables modular, traceable workflow orchestration.
- **FastAPI:** Modern, fast, and easy-to-use API framework.
- **Pydantic:** Ensures robust schema validation and type safety.
- **LangSmith:** Provides detailed execution traces for debugging and optimization.
- **SQLite:** Lightweight, file-based persistence for checkpoints and logs.

---

## 4. Schema Definitions and Validation Strategy

All data entering and leaving the system is validated using Pydantic models defined in `src/schemas.py`. This ensures:

- Type safety
- Clear error messages
- Consistent API/CLI outputs

**Example Schema:**
```python
from pydantic import BaseModel
from typing import List, Optional

class BriefRequest(BaseModel):
	 topic: str
	 depth: int
	 user_id: str

class BriefResponse(BaseModel):
	 title: str
	 summary: str
	 key_points: List[str]
	 # ... other fields ...
```

---

## 5. Execution Flow

1. **User submits a request** (API or CLI).
2. **Input is validated** using Pydantic schemas.
3. **Retriever gathers context** (if needed).
4. **LLM generates the brief** using LangChain orchestration.
5. **Output is validated** and formatted.
6. **Result is returned** to the user and optionally persisted.
7. **Trace is logged** via LangSmith for observability.

---

## 6. Deployment Instructions

### Local Development

1. Clone the repository:
	```bash
	git clone https://github.com/Zeeshan2912/atomicads-brief-gen.git
	cd atomicads-brief-gen
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Configure environment variables:
	- Copy `.env.example` to `.env` and fill in your keys.
4. Start the API server:
	```bash
	uvicorn src.main:app --reload
	```
5. Use the CLI:
	```bash
	python src/cli.py --topic "Edge Computing" --depth 2 --user-id "zeeshan"
	```

### Docker Deployment

1. Build and run the Docker container:
	```bash
	docker build -t atomicads .
	docker run --env-file .env -p 8000:8000 atomicads
	```

---

## 7. Example Requests and Outputs

### API Example

**Request:**
```json
{
  "topic": "Edge Computing",
  "depth": 2,
  "user_id": "zeeshan"
}
```

**Response:**
```json
{
  "title": "The Future of Edge Computing",
  "summary": "Edge computing brings computation closer to the data source for faster processing...",
  "key_points": [
	 "Reduces latency",
	 "Supports real-time processing",
	 "Optimizes IoT performance"
  ]
}
```

### CLI Example

```bash
python src/cli.py --topic "Edge Computing" --depth 2 --user-id "zeeshan"
```

---

## 8. Cost and Latency Benchmarks

| Operation         | Avg Latency (ms) | Cost (USD/request) |
|-------------------|------------------|--------------------|
| Brief Generation  | 1200             | $0.002             |

*Benchmarks are based on test runs with OpenAI GPT-3.5 and may vary by model/provider.*

---

## 9. Limitations and Areas for Improvement

- Limited to supported LLM providers.
- No user authentication or rate limiting.
- Briefs may lack deep domain-specific nuance.
- Future work: add more models, improve retrieval, support multi-language, add user management.

---

## 10. Supporting Files

- `.env.example` – Environment variable template.
- `LICENSE` – Project license.
- `CONTRIBUTING.md` – Contribution guidelines.
- `Makefile` or `justfile` – (Optional) Automation for common tasks.

---

## 11. Tracing and Observability

LangSmith is integrated for full traceability. All requests and LLM executions are logged for debugging and optimization. See `docs/langsmith_trace1.png` and `docs/langsmith_trace2.png` for example traces.

---