from fastapi import FastAPI
from datetime import datetime, timezone
import random

from db import init_db, insert_test_message

app = FastAPI()


# -------------------------
# STARTUP (DB CONNECT)
# -------------------------
@app.on_event("startup")
async def startup():
    await init_db()


# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}


# -------------------------
# TEST DATA GENERATOR
# -------------------------
def generate_fake_message():
    return {
        "telegram_message_id": random.randint(1000, 999999),
        "channel_id": -100123456789,
        "channel_title": "PGA News Monitor",
        "message_text": f"TEST MESSAGE {random.randint(1,1000)}",
        "message_date": datetime.now(timezone.utc),

        "sender_id": random.randint(10000, 99999),
        "sender_username": "test_user",

        "raw_update": {
            "source": "azure_test_endpoint",
            "type": "synthetic"
        }
    }


# -------------------------
# TEST ENDPOINT (MAIN EXPERIMENT)
# -------------------------
@app.get("/test-insert")
async def test_insert():

    data = generate_fake_message()

    await insert_test_message(data)

    return {
        "status": "ok",
        "inserted": data
    }
