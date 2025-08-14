from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
import os

async def get_checkpointer():
    db_path = os.getenv("DATABASE_URL", "sqlite:///./checkpoints.db").replace("sqlite:///", "")
    async with AsyncSqliteSaver.from_conn_string(db_path) as saver:
        yield saver