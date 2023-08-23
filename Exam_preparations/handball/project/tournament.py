import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

import re

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    valid_equipments = {"KneePad": KneePad, "ElbowPad": ElbowPad}

    def __init__(self, name: str, capacity: int):
        self.name = name  # the name of the tournament
        self.capacity = capacity  # the number of teams the tournament can have
        self.equipment = []  # contain all object equipment
        self.teams = []  # contain all teams objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not list(re.finditer(r'^[a-zA-z0-9]+$', value)):
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if not self.valid_equipments.get(equipment_type):
            raise Exception("Invalid equipment type!")

        new_equipment = self.valid_equipments[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    @property
    def valid_teams(self):
        return {"OutdoorTeam": OutdoorTeam,
                "IndoorTeam": IndoorTeam
                }

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if not self.valid_teams.get(team_type):
            raise Exception("Invalid team type!")

        if self.capacity < len(self.teams) + 1:
            return "Not enough tournament capacity."

        new_team = self.valid_teams[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._get_equipment_by_type(equipment_type)
        team = self._get_team_by_name(team_name)[0]
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_list = self._get_team_by_name(team_name)
        if not team_list:
            raise Exception("No such team!")
        team = team_list[0]
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_prices = 0
        for e in self.equipment:
            if type(e).__name__ == equipment_type:
                e.increase_price()
                changed_prices += 1

        return f"Successfully changed {changed_prices}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_team_by_name(team_name1)[0]
        team2 = self._get_team_by_name(team_name2)[0]
        if type(team1).__name__ != type(team2).__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        result1 = team1.get_total_protection() + team1.advantage
        result2 = team2.get_total_protection() + team2.advantage

        the_winner = None
        if result1 > result2:
            the_winner = team1
        elif result2 > result1:
            the_winner = team2

        if not the_winner:
            return "No winner in this game."

        the_winner.win()
        return f"The winner is {the_winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        text = f"""Tournament: {self.name}
Number of Teams: {self.capacity}
Teams:""" + "\n"

        list_results = []
        for team_info in sorted_teams:
            list_results.append(team_info.get_statistics())
        text += "\n".join(list_results)
        return text

    # helper methods
    def _get_equipment_by_type(self, type_eq):  # will always exist
        equipment = [e for e in reversed(self.equipment) if type(e).__name__ == type_eq][0]
        return equipment

    def _get_team_by_name(self, team_name):
        team = [t for t in self.teams if t.name == team_name]
        if team:
            return team
