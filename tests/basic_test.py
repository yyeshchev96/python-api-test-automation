import httpx
import pytest
from assertpy import assert_that


def test_passing_scenario():
    assert_that(True).is_true()


@pytest.mark.xfail
def test_failing_scenario():
    assert_that(False).is_true()


def test_httpx_get_google_search_python_returns_200():
    resp = httpx.get("https://httpbin.org/json")
    assert_that(resp.status_code).is_equal_to(200)
