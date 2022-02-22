# Built-In
import json
from typing import Any
from io import BytesIO
from zipfile import ZipFile

from trii.utils.logs import set_logger

logger = set_logger(__name__)

def zip(data_input: dict, filename: str = None) -> BytesIO:
    data_bytes = json.dumps(data_input, indent=2).encode("utf-8")
    zip_buffer = BytesIO()
    with ZipFile(zip_buffer, "w") as zip_file:
        zip_file.writestr(f"{filename}.json", data_bytes)

    return zip_buffer
