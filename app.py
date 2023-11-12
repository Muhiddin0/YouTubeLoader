import asyncio
from fastapi import FastAPI
from Loader import Loader

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
    "http://localhost:3000/"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(url:str):
    asyncio.sleep(10)
    # asyncio.create_task(load_task(url))
    
    data = Loader.youtube(url)
    print(data)

    return data
