from intro.user import User


class Group:
    # class attribute
    groups = []

    group_id: int = 0
    group_name: str = ''
    is_active: bool = False
    has_admin_access: bool = False
    users: [User] = []

    def get_active_group_names(self):
        output = []
        for group in Group.groups:
            if group.is_active:
                output.append(group.group_name)
        return output

    def get_active_group_ids(self):
        output = []
        for group in Group.groups:
            if group.is_active:
                output.append(group.group_id)
        return output

    def get_admin_group_names(self):
        output = []
        for group in Group.groups:
            if group.has_admin_access:
                output.append(group.group_id)
        return output

    def get_admin_group_ids(self):
        output = []
        for group in Group.groups:
            if group.has_admin_access:
                output.append(group.group_id)
        return output
