import pytest
import sys

@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 7, 8),
        (2, 8, 10),
        pytest.param(3, 9, 12, id="3+9=12")
    ],
)
def test_parameters(a, b, expected):
    assert a+b == expected
