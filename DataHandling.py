# 29/12/2021 DataHandling
from dataclasses import dataclass
import pickle
from UserHandling import User




@dataclass
class Task:
    name: str
    desc: str
    complete: bool

    def __init__(self, task_name: str, task_desc):
        name = task_name
        desc = task_desc
        complete = False


@dataclass
class Group:
    group_name: str
    lead: User
    tasks: list[Task]
    members: list[User]

    def __init__(self, lead: User, name: str):
        group_name = name
        lead = lead
        tasks = []
        members = []



@dataclass
class Team:
    lead: User
    groups: list[Group]

    def __init__(self, lead: User):
        lead = lead
        groups = []


class DataHandler:

    def __init__(self):
        # self.import_data()
        # these will be saved later and imported later
        self.teams = []
        self.logins = {}

    def import_data(self):
        ...  # pickle load

    def create_new_team(self):
        ...


    def import_team(self, team_id: int) -> Team:
        return self.teams[team_id]



