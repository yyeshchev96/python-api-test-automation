import httpx
import pytest
from assertpy import assert_that

from api_core.builder import APIRequestBuilder
from api_core.client import HTTPXClient
from api_core.utils import APIMethods


@pytest.mark.always_green
def test_passing_scenario():
    assert_that(True).is_true()


@pytest.mark.xfail
def test_failing_scenario():
    assert_that(False).is_true()


@pytest.mark.google_search
def test_httpx_get_google_search_python_returns_301():
    response = httpx.get("https://google.com?q=selenium")

    assert_that(response.status_code).is_equal_to(301)


@pytest.mark.httpx_client
def test_custom_httpx_client():
    with HTTPXClient() as client:
        response = client.get("https://httpbin.org/json")

    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.httpx_builder
def test_example_of_httpx_builder():
    response = (
        APIRequestBuilder()
        .with_method(APIMethods.GET)
        .with_url("https://httpbin.org/json")
        .perform_request()
    )

    assert_that(response.status_code).is_equal_to(200)
