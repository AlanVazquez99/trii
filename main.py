# Third Party
import requests
from fastapi import FastAPI

# Internal
from trii.client import Client
from trii.utils.logs import set_logger

logger = set_logger(__name__)

app = FastAPI()
client = Client("https://rickandmortyapi.com/api", "Rick and Morty API")

@app.get("/{resource}")
async def read_item(resource: str):
    logger.debug(f"{client.name}/{resource}")
    return client.get(resource)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
