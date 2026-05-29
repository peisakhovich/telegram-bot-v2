from fastapi import FastAPI
print("AZURE VERSION 999")
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "running HELLO HELLO"}
