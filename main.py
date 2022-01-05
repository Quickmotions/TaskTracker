from program.teamHandling import Team
from program.userHandling import User
from program.commandHandling import use_command


# load teams
teams = []
current_user = None
current_team = None


def login(teams: list[Team], username: str, password: str):
    for team in teams:
        for _, user in team.users.items():
            if user.username.lower() == username.lower() and user.password == password:
                print(f"Logging in as {user.username}")
                return user, team
    print("Incorrect password or username")


def logged_in(user):
    print(f"------------{current_user.username}------------")
    while True:
        try:
            use_command(command=input(">>> "), team=current_team, user=current_user)
        except Exception as e:
            print(e)


while True:
    print("Type L to login\nType R to register a new Team")
    choice = input(">>>")
    if choice.lower() == "l":
        current_user, current_team = login(teams=teams, username=input("Username: "), password=input("Password: "))

        if current_user is not None:
            logged_in(user=current_user)

    if choice.lower() == "r":

        current_user = User(name=input("Full Name: "), perm_lvl=0)
        current_team = Team(team_name=input("Team Name: "))
        current_team.users[current_user.id] = current_user
        teams.append(current_team)




