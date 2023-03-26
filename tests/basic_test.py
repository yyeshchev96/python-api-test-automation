import pytest
from assertpy import assert_that


def test_passing_scenario():
    assert_that(True).is_true()


@pytest.mark.xfail
def test_failing_scenario():
    assert_that(False).is_true()
