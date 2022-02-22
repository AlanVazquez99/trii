# Built-In
from typing import Optional

# Third Party
import requests
from fastapi import FastAPI, Query, Request

# Internal
from trii.client import Client
from trii.utils.logs import set_logger

logger = set_logger(__name__)

app = FastAPI()
client = Client("https://rickandmortyapi.com/api", "Rick and Morty API")


@app.get("/{resource}/{id}")
@app.get("/{resource}")
async def get_resources(request: Request, resource: str, id: Optional[str] = Query("")):
    query_params = request.query_params
    route = f"{resource}/{id}?{query_params}"

    logger.debug(route)
    return client.get(route)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
