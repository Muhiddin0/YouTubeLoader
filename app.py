import asyncio
from fastapi import FastAPI
from Loader import Loader

app = FastAPI()


@app.get("/")
async def root(url:str):
    asyncio.sleep(10)
    # asyncio.create_task(load_task(url))
    
    data = Loader.youtube(url)
    print(data)

    return data
