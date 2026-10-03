from enum import Enum


class Permission(Enum):
    VIEW_RECORDS = "view_records"
    CREATE_RECORDS = "create_records"
    MODIFY_RECORDS = "modify_records"
    EXPORT_DATA = "export_data"
    MANAGE_USERS = "manage_users"
    AUTHORIZE_USB = "authorize_usb"
