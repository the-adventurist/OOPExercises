from typing import List

import project.player as Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[str: Player] = []

    def add_player(self, player: Player) -> str:
        this_player = [p for p in self.__players if player == p]
        if this_player:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str:
        this_player = [p for p in self.__players if p.name == player_name]
        if this_player:
            player = this_player[0]
            self.__players.remove(player)
            return player

        return f"Player {player_name} not found"

