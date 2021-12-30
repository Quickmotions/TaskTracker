# 29/12/2021 DataHandling
from dataclasses import dataclass
import pickle


@dataclass
class Team:
    team_id: str
    team_leader: str
    team_created: str
    team_groups: dict[dict[list]]  # TeamName{ PermissionGroup[ User1, User2 ] }
    team_tasks: dict[dict[dict[dict]]]  # ProjectName { TeamName{ TaskName{ TaskData } } }
    # These 2 lines above should be cleaned up into 2 new classes for tasks and groups rather than large dictionaries.


@dataclass
class DataHandler:
    teams: dict[Team]

    def __init__(self):
        self.import_data()

    def import_data(self):
        ...  # pickle load

    def import_team(self, team_id: str) -> Team:
        return self.teams[team_id]
