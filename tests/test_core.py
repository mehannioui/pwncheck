from pwncheck.core import get_leak_count


def test_get_leak_count():
    class FakeResponse:
        text = "ABCDEF12345:10\nZZZZZ999999:5"

    assert get_leak_count(FakeResponse, "12345") == 10
    assert get_leak_count(FakeResponse, "99999") == 5
    assert get_leak_count(FakeResponse, "00000") == 0
