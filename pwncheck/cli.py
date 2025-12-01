import argparse
import logging
from .core import check_password
from .utils import print_success, print_warning, secure_input

logger = logging.getLogger(__name__)


def run_interactive():
    print("Enter a password to check (hidden input):")
    pw = secure_input("> ")
    count = check_password(pw)

    if count > 0:
        print_warning(f"⚠️  Found {count} breaches! Change it immediately.")
    else:
        print_success("✅ Not found in any known breach.")


def run_cli(passwords):
    for pw in passwords:
        count = check_password(pw)
        if count > 0:
            print_warning(f"⚠️  Found {count} breaches!")
        else:
            print_success("✅ Safe: No breaches found.")


def main():
    parser = argparse.ArgumentParser(
        description="Check if your password was exposed in known breaches."
    )
    parser.add_argument(
        "passwords",
        nargs="*",
        help="Passwords to check. If empty, interactive mode starts.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging.",
    )

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.passwords:
        run_cli(args.passwords)
    else:
        run_interactive()
