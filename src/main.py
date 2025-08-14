import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from src.graph import graph
from src.schemas import FinalBrief

load_dotenv()
app = FastAPI()

class BriefRequest(BaseModel):
    topic: str
    depth: int = 1
    user_id: str

@app.post("/brief")
async def create_brief(req: BriefRequest):
    compiled = graph.compile()  # Removed checkpointer for now
    try:
        result = await compiled.ainvoke(
            {"topic": req.topic, "depth": req.depth, "user_id": req.user_id}
        )
        brief = FinalBrief(**result["final_brief"])
        return brief.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
