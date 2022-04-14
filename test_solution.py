import pytest
from solution import implementation


@pytest.mark.parametrize(
    "command, expected",
    [
        ("E", "E"),
    ],
)
def test_implementation(s, expected):
    print(f"{s} {expected}")
    answer = implementation(s)
    assert answer == expected
 