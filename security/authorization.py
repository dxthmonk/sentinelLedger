
from security.authentication import AccountStatus
from security.permissions import Permission
from security.role_permissions import ROLE_PERMISSIONS
from security.roles import Role


def has_permission(role: Role, permission: Permission) -> bool:
    """Check whether a role includes a permission."""
    return permission in ROLE_PERMISSIONS.get(role, set())


def user_has_permission(user, permission: Permission) -> bool:
    """Allow an action only when the account is active and authorized."""
    if user is None:
        return False

    if user.status != AccountStatus.ACTIVE:
        return False

    return has_permission(user.role, permission)
