import requests
import hashlib
import logging

API_URL = "https://api.pwnedpasswords.com/range/"
TIMEOUT = 5

logger = logging.getLogger(__name__)


def request_api_data(prefix: str) -> requests.Response:
    """Query pwnedpasswords API for the first 5 chars of SHA1 hash."""
    logger.debug(f"Requesting API data for prefix: {prefix}")
    try:
        r = requests.get(API_URL + prefix, timeout=TIMEOUT)
        r.raise_for_status()
        return r
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {e}")
        raise RuntimeError(f"Network error: {e}")


def get_leak_count(hashes: requests.Response, suffix: str) -> int:
    """Return leak count for the given SHA1 suffix."""
    for line in hashes.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)
    return 0


def check_password(password: str) -> int:
    """Check password against Pwned Passwords breaches."""
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    response = request_api_data(prefix)
    return get_leak_count(response, suffix)
