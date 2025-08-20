import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from src.graph import graph
from src.schemas import FinalBrief

# Load environment variables
load_dotenv()

# ✅ Enable LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# ✅ Health Check Endpoint
@app.get("/")
async def health_check():
    return {"status": "ok", "message": "AtomicAds Brief Generator API is running!"}

# Request Model
class BriefRequest(BaseModel):
    topic: str
    depth: int = 1
    user_id: str

# ✅ Generate Brief Endpoint
@app.post("/brief")
async def create_brief(req: BriefRequest):
    compiled = graph.compile()
    try:
        result = await compiled.ainvoke(
            {"topic": req.topic, "depth": req.depth, "user_id": req.user_id}
        )
        brief = FinalBrief(**result["final_brief"])
        return brief.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
