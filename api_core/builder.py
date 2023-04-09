from __future__ import annotations

import logging

from httpx import Response

from api_core.client import HTTPXClient
from api_core.utils import APIMethods

_logging = logging.getLogger(__name__)


class APIRequestBuilder:
    def __init__(self) -> None:
        _logging.info("Creating new APIRequestBulder")

        self._client = HTTPXClient()
        self._method = None
        self._headers = None
        self._auth = None
        self._body = None

    def with_method(self, api_method: APIMethods) -> APIRequestBuilder:
        _logging.info(f"Setting method: {api_method}")
        self._method = api_method
        return self

    def with_headers(self, headers: dict) -> APIRequestBuilder:
        _logging.info(f"Setting headers: {headers}")
        self._headers = headers
        return APIRequestBuilder

    def with_url(self, url: str) -> APIRequestBuilder:
        _logging.info(f"Setting url: {url}")
        self._url = url
        return self

    def with_auth(self, auth) -> APIRequestBuilder:
        _logging.info(f"Setting auth: {auth}")
        self._auth = auth
        return self

    def with_body(self, body) -> APIRequestBuilder:
        _logging.info(f"Setting body: {body}")
        self._body = body
        return self

    def perform_request(self) -> Response:
        _logging.info("Executing request")

        with self._client as httpx_client:
            return httpx_client.request(
                self._method,
                url=self._url,
                headers=self._headers,
                content=self._body,
                auth=self._auth,
            )
