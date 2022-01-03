from program.userHandling import login, create_user
from program.teamHandling import Team
from program.commandHandling import use_command


# load users
teams = {}
current_user = None
current_team = None


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

        current_user = create_user()
        current_team = Team(lead=current_user, team_name=input("Team Name: "))
        # store new team and user to data dictionary
        current_team.users[current_user.id] = current_user
        teams[current_team.id] = current_team


