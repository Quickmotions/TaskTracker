# 29/12/2021 DataHandling
from dataclasses import dataclass
from program.userHandling import User


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
