from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def __init__(self):
        self.name: str = "None"
        self.perm_lvl: int = 0
        self.username: str = ""
        self.password: str = ""
        self.id: str = ""
        self.options: list = []
        self.commands = None
        self.current_group = None

    @abstractmethod
    def request_command(self):
        ...


class Team(ABC):
    @abstractmethod
    def __init__(self):
        self.lead = User
        self.groups = {}
        self.name = ""
        self.users = {}
        self.id = ""

    @abstractmethod
    def create_group(self):
        ...
