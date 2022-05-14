from starlette import status
import uvicorn
import hikari

from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, RedirectResponse
from tortoise.contrib.fastapi import register_tortoise
from cashews import cache

from config import tortoise_config
from api import router

cache.setup("mem://?check_interval=10&size=10000")
app = FastAPI()
app.include_router(router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = JSONResponse({"detail": "Not authenticated"}, status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        response = await call_next(request)
    except hikari.errors.UnauthorizedError:
        pass
    return response

origins = [
    "https://crypto.asuscomm.com",
    "https://crypto.asuscomm.com:80",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    config=tortoise_config,
    add_exception_handlers=True,
    generate_schemas=True
)

if __name__ == '__main__':
    uvicorn.run(
        'backend.main:app',
        host="192.168.1.88",
        port=8080,
        reload=True,
        ssl_keyfile='key.pem',
        ssl_certfile='cert.pem'
    )