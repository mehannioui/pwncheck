from pwncheck.utils import Colors


def test_colors_exist():
    assert hasattr(Colors, "GREEN")
    assert hasattr(Colors, "RED")
    assert hasattr(Colors, "RESET")
