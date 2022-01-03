from datetime import datetime
import random
from program.abstract import Team

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

commands_User = {
    'h': 'Help',  # shows all commands user has access too
    'v': 'View',  # shows dashboard which shows important data
    'l': 'List',  # shows members in your current group
    'i': 'Info',  # view details about yourself or another user

}


class User:
    def __init__(self, name, perm_lvl=0):
        self.name = name
        self.perm_lvl = perm_lvl
        date = datetime.now().date()
        self.username = name[0].upper() + name.split()[1] + date.strftime("%Y")
        print(f"Your username is {self.username}")
        self.password = str(input("Please enter a password: "))
        self.id = self.username + self.password + date.strftime("%Y") + str(random.randint(1, 9999))
        self.options = ["View Team", ""]
        self.commands = commands_User
        self.load_commands(self)
        self.current_group = None

    def load_commands(self, user):
        if user.perm_lvl < 2:
            self.commands.update(commands_lead)
        if user.perm_lvl < 1:
            self.commands.update(commands_root)


def login(teams: dict[Team], username: str, password: str):
    for team_id, team in teams.items():
        for _, user in team.users.items():
            if user.username.lower() == username.lower() and user.password == password:
                print(f"Logging in as {user.username}")
                return user, team
    print("Incorrect password or username")


def create_user(permission_level=0):
    return User(name=input("Users Full Name: "), perm_lvl=permission_level)
