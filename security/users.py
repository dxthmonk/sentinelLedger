from dataclasses import dataclass
from security.roles import Role


@dataclass
class User:
    user_id: str
    username: str
    role: Role
    approved: bool = False
    active: bool = True
