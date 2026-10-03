from security.permissions import Permission
from security.roles import Role


ROLE_PERMISSIONS = {
    Role.ADMINISTRATOR: {
        Permission.VIEW_RECORDS,
        Permission.CREATE_RECORDS,
        Permission.MODIFY_RECORDS,
        Permission.EXPORT_DATA,
        Permission.MANAGE_USERS,
        Permission.AUTHORIZE_USB,
    },

    Role.ANALYST: {
        Permission.VIEW_RECORDS,
        Permission.CREATE_RECORDS,
        Permission.MODIFY_RECORDS,
        Permission.EXPORT_DATA,
    },

    Role.VIEWER: {
        Permission.VIEW_RECORDS,
    },
}
