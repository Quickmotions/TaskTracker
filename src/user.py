import random
from datetime import datetime

from src.commands import Commands


class User:
    def __init__(self, name, perm_lvl=0):
        self.name = name
        self.perm_lvl = perm_lvl
        date = datetime.now().date()
        self.username = name[0].upper() + name.split()[1] + date.strftime("%Y")
        print(f"Your username is {self.username}")
        self.password = str(input("Please enter a password: "))
        self.id = self.username + self.password + date.strftime("%Y") + str(random.randint(1, 9999))
        self.commands = Commands(self)
        self.current_group = None
        print("DEBUG: Created New User")
