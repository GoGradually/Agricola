"""
새 라운드 카드 공개
"""
from command import Command



class OpenNewRoundCard(Command):
    def execute(self):
        game_status_repository.get_game_status().opened_round[game_status_repository.get_game_status().now_round] = True

    def log(self):
        pass
