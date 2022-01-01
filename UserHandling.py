from dataclasses import dataclass
from datetime import datetime
import random


class User:
    def __init__(self, name, perm_lvl=0):
        self.name = name
        self.perm_lvl = perm_lvl
        date = datetime.now().date()
        self.username = name[0].upper() + name.split()[1] + date.strftime("%Y")
        print(f"Your username is {self.username}")
        self.password = input("Please enter a password: ")
        self.id = self.username + self.password + date.strftime("%Y") + str(random.randint(1, 100))
        self.options = ["View Team", ""]
        if perm_lvl == 0:
            self.options.append("")

def login(users: list[User], username: str, password: str):
    for user in users:
        if user.username.lower() == username.lower() and user.password == password:
            print(f"Logging in as {user.username}")
            return user
    print("Incorrect password or username")
