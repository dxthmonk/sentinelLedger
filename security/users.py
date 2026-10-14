
from dataclasses import dataclass
from security.roles import Role
from security.authentication import AccountStatus


@dataclass
class User:
    user_id: str
    username: str
    role: Role
    status: AccountStatus = AccountStatus.PENDING
