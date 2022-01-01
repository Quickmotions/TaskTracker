from DataHandling import DataHandler
from UserHandling import User, login

# load users
users = []
current_user = None


def logged_in(user):
    print(f"------------{current_user.username}------------")
    while True:
        print(f"Options:\n"
              f"")

while True:
    print("Type L to login\nType R to register a new Team")
    choice = input(">>>")
    if choice.lower() == "l":
        current_user = login(users, input("Username: "), input("Password: "))
        if current_user is not None:
            logged_in(current_user)
    if choice.lower() == "r":
        users.append(User(input("Team Lead Name: "), perm_lvl=0))