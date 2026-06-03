import asyncpg
from config import DATABASE_URL

db_pool = None


async def init_db():
    global db_pool

    db_pool = await asyncpg.create_pool(
        DATABASE_URL,
        min_size=1,
        max_size=5
    )


async def insert_test_message(data: dict):
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO channel_messages_log (
                telegram_message_id,
                channel_id,
                channel_title,
                message_text,
                message_date,
                sender_id,
                sender_username,
                raw_update
            )
            VALUES ($1,$2,$3,$4,$5,$6,$7,$8)
            """,
            data["telegram_message_id"],
            data["channel_id"],
            data["channel_title"],
            data["message_text"],
            data["message_date"],
            data["sender_id"],
            data["sender_username"],
            data["raw_update"]
        )
