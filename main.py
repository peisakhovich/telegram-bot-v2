from fastapi import FastAPI
from datetime import datetime
import db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-insert")
async def test_insert():
    await db.insert_message({
        "channel_name": "pga_news_monitor",
        "message_text": "test message from azure",
        "username": "system",
        "user_id": "0",
        "timestamp": datetime.utcnow()
    })
    return {"insert": "ok"}
