"""
새 라운드 카드 공개
"""
from command import Command
import repository.game_status_repository as game_status_repository


class OpenNewRoundCard(Command):
    def execute(self):
        game_status_repository.game_status_repository.game_status.opened_round[game_status_repository.game_status_repository.game_status.now_round] = True

    def log(self):
        pass
