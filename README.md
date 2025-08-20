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

## **💻 CLI Usage**

Run the CLI tool:

```bash
python src/cli.py --topic "Edge Computing" --depth 2 --user_id "zeeshan"
```

**Example Output:**

```
Generated Brief:
Edge computing brings computation and data storage closer to devices where it is being gathered...
```

---

## **🌐 Deployed API**

**Live URL:** [https://atomicads-brief-gen-api.onrender.com]

✅ **Sample Request**
curl -X POST "https://atomicads-api.onrender.com/brief" \
-H "Content-Type: application/json" \
-d '{"topic":"Edge Computing","depth":2,"user_id":"zeeshan"}'

✅ **Sample Response**
{
  "title": "The Future of Edge Computing",
  "summary": "Edge computing brings computation closer to the data source for faster processing...",
  "key_points": [
    "Reduces latency",
    "Supports real-time processing",
    "Optimizes IoT performance"
  ]
}

---

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


