from enum import auto

from utils.enums import StrEnum


class APIMethods(StrEnum):
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()
