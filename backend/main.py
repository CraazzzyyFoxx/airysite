from typing import Optional

import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(
        'backend.main:app',
        host="192.168.1.88",
        port=80,
        reload=True,
    )
