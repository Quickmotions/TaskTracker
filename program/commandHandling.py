import random
import sys
from program.abstract import Team, User
from program.userHandling import User

from commands import *

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
    # TODO: move each command to separate file later



try:
    function = sys.argv[1]
    print(function)
    globals()[function]()
except IndexError:
    raise Exception("Please provide function name")
except KeyError:
    raise Exception("Function {} hasn't been found".format(function))