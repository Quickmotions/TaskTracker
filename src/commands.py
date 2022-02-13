from src.abstractBC import Team, User
import src.commands_list

commands_root = {
    'tl': commands_list.TeamList,  # shows all members in all groups
    'cg': commands_list.CreateGroup,  # create a team in your team
    'rg': commands_list.RemoveGroup, # remove a group from your team
    'gl': commands_list.GroupList, # show all groups in team
    'eg': commands_list.EditGroup, # select a group to edit

}
commands_lead = {
    'rm': commands_list.RemoveMember, # remove a member from your group
    'cm': commands_list.CreateMember, # create a member in your current group
    'mm': commands_list.MoveMember, # move a member into a group
}

commands_user = {
    'h': commands_list.Help,  # shows all commands_list user has access too
    'v': commands_list.View,  # shows dashboard which shows important data
    'l': commands_list.List,  # shows members in your current group
    'i': commands_list.Info,  # view details about yourself or another user

}

command_desc = {
    'tl': "shows all members in all groups",
    'cg': "create a team in your team",
    'Remove Group': "remove a group from your team",
    'Group List': "shows all groups in team",
    'Remove Member': "remove a member from your group",
    'Create Member': "create a member in your current group",
    'Help': "shows all commands_list user has access too",
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
    if command in commands_root or command in commands_user or command in commands_lead:
        if command in user.commands:
            process = user.commands[command]
            process()
        else:
            print("Invalid Permission")
    else:
        print("Invalid Command")


