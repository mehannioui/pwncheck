from getpass import getpass


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"


def print_success(msg):
    print(f"{Colors.GREEN}{msg}{Colors.RESET}")


def print_warning(msg):
    print(f"{Colors.RED}{msg}{Colors.RESET}")


def secure_input(prompt="Password: "):
    """Hidden terminal input."""
    return getpass(prompt)
