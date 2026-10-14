import hashlib
import hmac
import secrets


# Initial PBKDF2 work factor. Review and benchmark before production.
PBKDF2_ITERATIONS = 600_000
SALT_BYTES = 16
KEY_BYTES = 32
HASH_NAME = "sha256"


def create_password_verifier(password: str) -> dict[str, str | int]:
    """Create a salted password verifier. Never store the password itself."""
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")

    salt = secrets.token_bytes(SALT_BYTES)
    derived_key = hashlib.pbkdf2_hmac(
        HASH_NAME,
        password.encode("utf-8"),
        salt,
        PBKDF2_ITERATIONS,
        dklen=KEY_BYTES,
    )

    return {
        "algorithm": "pbkdf2_hmac_sha256",
        "iterations": PBKDF2_ITERATIONS,
        "salt": salt.hex(),
        "verifier": derived_key.hex(),
    }


def verify_password(password: str, record: dict[str, str | int]) -> bool:
    """Check a password against a previously created verifier."""
    if not isinstance(password, str) or not isinstance(record, dict):
        return False

    try:
        if record["algorithm"] != "pbkdf2_hmac_sha256":
            return False

        iterations = record["iterations"]
        if (
            not isinstance(iterations, int)
            or isinstance(iterations, bool)
            or not 1 <= iterations <= 2_000_000
        ):
            return False

        salt = bytes.fromhex(record["salt"])
        expected = bytes.fromhex(record["verifier"])

        if len(salt) != SALT_BYTES or len(expected) != KEY_BYTES:
            return False

        actual = hashlib.pbkdf2_hmac(
            HASH_NAME,
            password.encode("utf-8"),
            salt,
            iterations,
            dklen=KEY_BYTES,
        )

        return hmac.compare_digest(actual, expected)

    except (KeyError, TypeError, ValueError):
        return False
