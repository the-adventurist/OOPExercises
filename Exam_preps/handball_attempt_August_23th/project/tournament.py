from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}
    VALID_EQUIPMENTS = {"KneePad": KneePad, "ElbowPad": ElbowPad}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENTS:
            raise Exception("Invalid equipment type!")

        new_equipment_to_add = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(new_equipment_to_add)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."

        new_team_to_add = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team_to_add)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        list_team = self._get_team_by_name_in_list(team_name)
        team = list_team[0]
        current_equipment = [e for e in reversed(self.equipment) if type(e).__name__ == equipment_type][0]
        if team.budget < current_equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(current_equipment)
        team.equipment.append(current_equipment)
        team.budget -= current_equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_list = self._get_team_by_name_in_list(team_name)

        if not team_list:
            raise Exception("No such team!")

        team = team_list[0]
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        increased_prices = 0
        for current_equipment in self.equipment:
            if type(current_equipment).__name__ == equipment_type:
                increased_prices += 1
                current_equipment.increase_price()

        return f"Successfully changed {increased_prices}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_team_by_name_in_list(team_name1)[0]
        team2 = self._get_team_by_name_in_list(team_name2)[0]

        if type(team1).__name__ != type(team2).__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        protection1= sum(p for p in e)

        result1 = team1.advantage + sum(p for p in team1.equipment.protection)
        result2 = team2.adventage + sum(p for p in team2.equipment.protection)

        the_winner = None
        if result1 > result2:
            the_winner = team1
        elif result2 > result1:
            the_winner = team1
        else:
            return "No winner in this game."

        the_winner.win()
        return f"The winner is {the_winner.name}."





    # helper methods
    def _get_team_by_name_in_list(self, t_name):  # the team couldn't exist
        list_team = [t for t in self.teams if t.name == t_name]
        return list_team
