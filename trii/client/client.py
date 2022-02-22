# Built-In
import json
from typing import Union, Any, Literal
from json.decoder import JSONDecodeError

# Third Party
from requests.models import Response
import requests

# Internal
from trii.utils.logs import set_logger

logger = set_logger(__name__)


class Client:
    headers = {"Content-type": "application/json", "Accept": "text/plain"}

    def __init__(self, url_base: str, name: str = "Default") -> None:
        self.url_base = url_base
        self.name = name

    @property
    def url_base(self) -> str:
        return self._url_base

    @url_base.setter
    def url_base(self, url_base) -> None:
        self._url_base = url_base

    @property
    def name(self) -> str:
        return self._url_base

    @name.setter
    def name(self, name) -> None:
        self._name = name

    def __repr__(self) -> str:
        return f"<Client name={self.name} base={self.url_base}>"

    def get_url(self, route: str) -> str:
        url = f"{self.url_base}/{route}"
        if not self.validate_url(url):
            error_message = f"The URL protocol must be http or https: {url}"
            logger.error(error_message)
            raise ValueError(error_message)

        return url

    def get(self, route: str, **request_kwargs) -> dict[str, Any]:
        url = self.get_url(route)
        logger.info("Fetching: %s", url)
        response = requests.get(url, headers=self.headers, **request_kwargs)

        status_code = response.status_code
        logger.debug("Status Code: %s", response)
        data_out: dict[str, Any] = {
            "status": status_code,
            "message": "Request Successful",
            "data": self.get_response(response),
        }

        if status_code >= 300:
            error_message = f"There was a problem fetching the data from {url}"
            data_out["message"] = error_message
            logger.error(error_message)

        return data_out

    @classmethod
    def get_response(cls, response: Response) -> Union[str, dict]:
        try:
            content = response.json()
        except JSONDecodeError:
            content = response.text
        return content

    @staticmethod
    def validate_url(url) -> bool:
        return url.startswith("http")
