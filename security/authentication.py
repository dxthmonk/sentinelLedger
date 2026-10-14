
from enum import Enum

from security.credentials import verify_password


class AccountStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    ACTIVE = "active"
    DISABLED = "disabled"


def authenticate_user(user, credential_record, password):
    """Authenticate an active user against a stored password verifier."""

    if user is None:
        return False

    if user.status != AccountStatus.ACTIVE:
        return False

    if not verify_password(password, credential_record):
        return False

    return True
