import random

from program.abstract import Team, User
from program.teamHandling import Group
from program.userHandling import create_user

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

    if command == "Help":
        for key, option in user.commands.items():
            print(f"{key} - {command_desc[option]}")

    if command == "Info":
        print(f"Name: {user.name}\n"
              f"Username: {user.username}\n"
              f"Password: {user.password}\n"
              f"Commands: {list_commands(user)}\n"
              f"ID: {user.id}")

    if command == "Create Group":
        if len(args) > 0:
            group_name = args[0]
            if group_name not in team.groups:
                new_group = Group(lead=user, group_name=group_name)
                team.groups[new_group.id] = new_group
                print(f"Created Group: {new_group.name} with ID: {new_group.id}")
                return
            else:
                print(f"Group named: {group_name} already exists")
        print("Specify the name of the group as:\n"
              "cg (group name)")

    if command == "Edit Group":
        if len(args) > 0:
            group_id = args[0]
            if group_id in team.groups:
                user.current_group = team.groups[group_id]
                print(f"Now editing {user.current_group.name}")
                return
        print("Unable to find group\n"
              "Specify the id of the group as:\n"
              "eg (group id)")

    if command == "Team List":
        for user_id, user in team.users.items():
            print(f"({user_id}) {user.name}")

    if command == "Create Member":
        try:
            new_member = create_user(permission_level=input("Permission Level\n"
                                                            "(0=root, 1=lead, 2=user\n"
                                                            ">>> "))
            team.users[new_member.id] = new_member
            print(
                f"Created: {new_member.name} with ID: {new_member.id} and permission level: {new_member.perm_lvl}")
        except Exception as e:
            print(e)

    if command == "Move Member":
        try:
            selected_group = input("Group ID: ")
            if selected_group in team.groups:
                selected_user = input("Member ID: ")
                if selected_user in team.users:
                    selected_user = team.users[selected_user]
                    team.groups[selected_group].members.append(selected_user.id)
                    print(f"Added {selected_user.name} to {team.groups[selected_group].name}")
                else:
                    print(f"Unable to find user with ID: {selected_user}")
                    return
            else:
                print(f"Unable to find group with ID: {selected_group}")
                return

        except Exception as e:
            print(e)
