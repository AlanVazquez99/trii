# Built-In
from typing import Optional

# Third Party
import requests
from fastapi import FastAPI, Query, Request
from fastapi.responses import FileResponse, StreamingResponse

# Internal
from trii.client import Client
from trii.utils.logs import set_logger
from trii.utils.zip import zip


logger = set_logger(__name__)

app = FastAPI()
client = Client("https://rickandmortyapi.com/api", "Rick and Morty API")


@app.get("/{resource}/{id}")
@app.get("/{resource}")
async def get_resources(
    request: Request,
    resource: str,
    id: Optional[str] = Query(""),
    download: bool = False,
):
    query_params = request.query_params
    route = f"{resource}/{id}"
    uri = f"{route}?{query_params}"

    logger.debug(uri)
    data = client.get(uri)

    if download:
        io = zip(data, route)
        headers = {
            "Content-Disposition": f"attachment; filename=\"{route}.zip\""
        }
        return StreamingResponse(iter([io.getvalue()]), headers=headers)
    return data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
