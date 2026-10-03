from security.permissions import Permission
from security.role_permissions import ROLE_PERMISSIONS
from security.roles import Role


def has_permission(role: Role, permission: Permission) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())
