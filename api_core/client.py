import logging

import httpx

_logging = logging.getLogger(__name__)


def log_request(request: httpx.Request):
    _logging.info(f"REQUEST: [{request.method} | {request.url}] - Waiting for response")


def log_response(response: httpx.Response):
    request = response.request
    _logging.info(f"RESPONSE: [{request.method} | {request.url}] - Status {response.status_code}")


class HTTPXClient(httpx.Client):
    def __init__(self, *args, **kwargs):
        self._hooks = {"request": [log_request], "response": [log_response]}
        super().__init__(event_hooks=self._hooks, *args, **kwargs)
