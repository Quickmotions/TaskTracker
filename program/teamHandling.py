from datetime import datetime
import random
from program.abstract import User

date = datetime.now().date()


class Task:

    def __init__(self, task_name: str, task_desc: str):
        self.name: task_name
        self.desc: task_desc
        self.complete: False


class Group:

    def __init__(self, lead: User, group_name: str):
        self.name = group_name
        self.lead = lead
        self.id = group_name[0] + date.strftime("%Y") + str(random.randint(1, 9999))
        self.tasks = []
        self.members = []


class Team:

    def __init__(self, lead: User, team_name: str):
        self.lead = lead
        self.groups = {}
        self.users = {}
        self.name = team_name
        self.id = team_name[0] + date.strftime("%Y") + str(random.randint(1, 9999))
