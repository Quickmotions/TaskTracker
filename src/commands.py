from src.abstract import Team
from src.user import User

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

command_desc = {
    'Team List': "shows all members in all groups",
    'Create Group': "create a team in your team",
    'Remove Group': "remove a group from your team",
    'Group List': "shows all groups in team",
    'Remove Member': "remove a member from your group",
    'Create Member': "create a member in your current group",
    'Help': "shows all commands user has access too",
    'View': "shows dashboard which shows important data",
    'List': "shows members in your current group",
    'Info': "view details about yourself or another user",
    'Edit Group': "select a group to edit",
    'Move Member': "move a member into a group",
}


class Commands:
    def __init__(self, user: User):
        self.list = commands_user
        if user.perm_lvl < 2:
            self.list.update(commands_lead)
        if user.perm_lvl < 1:
            self.list.update(commands_root)


def use_command(command: str, team: Team, user: User):
    command = command.split()
    args = command[1:]
    command = command[0]
    if command in user.commands:
        process(user.commands[command], team, user, args)
    else:
        print("Unknown command (use h for help)")


def list_commands(user: User) -> str:
    command_list = ""
    for key, command in user.commands.items():
        command_list += f"{key}, "
    command_list = command_list[:-2]
    return command_list


def process(command: str, team: Team, user: User, args: list[str]):
    """EMPTY WORK IN PROGRESS"""
    pass

