from src.schemas import FinalBrief
from datetime import datetime

def test_valid_brief():
    brief = FinalBrief(
        topic="AI",
        depth=1,
        summary="Summary",
        key_findings=["a"],
        sources=[{"title":"t","url":None,"snippet":"s"}],
        plan=["step1"],
        metadata={"tokens":100},
        generated_at=datetime.utcnow()
    )
    assert brief.topic == "AI" 