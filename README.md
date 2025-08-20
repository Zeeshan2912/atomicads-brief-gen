# **AtomicAds – Gen AI Developer Assignment**

---

## **📌 Overview**

AtomicAds is a **Generative AI-powered advertising brief generator** designed to help businesses and marketers create concise, targeted ad briefs using LLMs. It provides both **API** (FastAPI) and **CLI** interfaces and integrates with **LangSmith** for traceability and debugging.

---

## **✅ Features**

* **AI-Powered Brief Generation** using LangChain and LLMs.
* **FastAPI REST API** for programmatic access.
* **Command-Line Interface (CLI)** for quick usage.
* **LangSmith Trace Integration** for detailed execution logs.
* **Modular Design** with clear separation of concerns.

---

## **📂 Project Structure**

```
AtomicAds/
│   .env.example         # Environment variables template
│   Dockerfile           # For containerized deployment
│   requirements.txt     # Project dependencies
│   README.md            # Documentation
│
├───docs/
│       architecture.md   # Detailed design and architecture
│       sample_request.json
│       sample_response.json
│
├───src/
│   │   main.py          # FastAPI entry point
│   │   cli.py           # CLI entry point
│   │   graph.py         # Workflow orchestration
│   │   llms.py          # LLM configuration and calls
│   │   persistence.py   # Data persistence layer
│   │   retriever.py     # Information retrieval utilities
│   │   schemas.py       # Pydantic models
│   │   search_tools.py  # Search helper functions
│
└───tests/
        test_api.py       # API test cases
        test_schemas.py   # Schema validation tests
```

---

## **🛠 Tech Stack**

* **Language:** Python 3.12
* **Framework:** FastAPI
* **AI Orchestration:** LangChain
* **LLM Provider:** OpenAI (or equivalent)
* **Deployment:** Render / Docker
* **Tracing:** LangSmith
* **Testing:** Pytest

---

## **⚙️ Setup Instructions**

### **1. Clone Repository**

```bash
git clone https://github.com/Zeeshan2912/atomicads-brief-gen.git
cd atomicads-brief-gen
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**

Create a `.env` file from `.env.example` and update:

```
xGROQ_API_KEY=your_groq_api_key
PRIMARY_GROQ_MODEL=llama-3.3-70b-versatile
FALLBACK_GROQ_MODEL=llama-3.1-8b-instant
SERPAPI_API_KEY=your_serpapi_key
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_TRACING=true
DATABASE_URL=sqlite:///./checkpoints.db

```

---

## **🚀 Running the API**

### **Start the API Server**

```bash
uvicorn src.main:app --reload
```

### **API Endpoints**

**POST** `/generate`

* **Request Example:**

```json
{
  "topic": "Edge Computing",
  "depth": 2,
  "user_id": "zeeshan"
}
```

* **Expected Response:**

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

---

## **🌐 Deployed API**

**Live URL:** [https://atomicads-brief-gen-api.onrender.com]

✅ **Sample Request**
 $ curl -X POST "https://atomicads-brief-gen-api.onrender.com/brief" \
-H "Content-Type: application/json" \
-d '{"topic":"Edge Computing","depth":2,"user_id":"zeeshan"}' | jq

✅ **Sample Response**
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   572    0   516  100    56   1461    158 --:--:-- --:--:-- --:--:--  1625
{
  "topic": "Edge Computing",
  "depth": 2,
  "summary": "This is a mock summary for topic 'Edge Computing' with depth 2.",
  "key_findings": [
    "Finding 1",
    "Finding 2",
    "Finding 3"
  ],
  "sources": [
    {
      "title": "Mock Source 1",
      "url": "http://example.com/",
      "snippet": "Snippet about the topic.",
      "rank": null
    },
    {
      "title": "Mock Source 2",
      "url": "http://example.com/",
      "snippet": "Another snippet.",
      "rank": null
    }
  ],
  "plan": [
    "Step 1: Research",
    "Step 2: Summarize",
    "Step 3: Validate"
  ],
  "metadata": {
    "tokens_used": 500
  },
  "generated_at": "2025-08-13T15:30:00+00:00"
}

---

## 💻 **CLI Usage**

You can use the CLI to generate an ad brief directly from the terminal.

### ✅ Run the API (if using local host)
```bash
uvicorn src.main:app --reload

✅ Use the CLI
 bash
python src/cli.py --topic "Edge Computing" --depth 2 --user-id "zeeshan"

✅ Example Output:
json

{
  "title": "The Future of Edge Computing",
  "summary": "Edge computing brings computation closer to the data source for faster processing...",
  "key_points": [
    "Reduces latency",
    "Supports real-time processing",
    "Optimizes IoT performance"
  ]
}

----
## **📺 Demo Video**

**Watch here:** \[Insert YouTube or Google Drive Link] *(Update after recording)*

---

## **📊 LangSmith Trace**

* **Trace Link:** \[Insert LangSmith Trace URL]
* **Screenshot:** *(Add screenshot image here)*

---

## **📐 Architecture Diagram**

```mermaid
graph TD
A[User Input] --> B[FastAPI Endpoint]
B --> C[LangChain Pipeline]
C --> D[LLM Model]
D --> E[Generated Brief]
```

---

## **🔮 Future Enhancements**

* Add multiple ad formats (social, video, display ads).
* Support for multilingual briefs.
* Fine-tuned models for industry-specific briefs.

---

## **👨‍💻 Author**

**Mohammed Zeeshan Khan**
📧 Email: \[mohammedzeeshankhan1999@gmail.com]
🔗 GitHub: \[https://github.com/Zeeshan2912]

---


