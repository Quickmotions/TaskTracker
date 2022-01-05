from abstract import User

commands_root = {
    'tl': 'Team List',  # shows all members in all groups
    'cg': 'Create Group',  # create a team in your team
    'rg': 'Remove Group',  # remove a group from your team
    'gl': 'Group List',  # shows all groups in team
    'eg': 'Edit Group',  # select a group to edit

}
commands_lead = {
    'rm': 'Remove Member',  # remove a member from your group
    'cm': 'Create Member',  # create a member in your current group
    'mm': 'Move Member',  # move a member into a group
}

commands_user = {
    'h': 'Help',  # shows all commands user has access too
    'v': 'View',  # shows dashboard which shows important data
    'l': 'List',  # shows members in your current group
    'i': 'Info',  # view details about yourself or another user

}


class Commands:
    def __init__(self, user: User):
        self.list = commands_user
        if user.perm_lvl < 2:
            self.list.update(commands_lead)
        if user.perm_lvl < 1:
            self.list.update(commands_root)
