"""
undo point 를 저장하는 커맨드
"""
from command import Command
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_status_repository
import repository.round_status_repository as round_status_repository
from repository.undo_repository import undo_repository


class SaveUndoPoint(Command):
    def execute(self):
        undo_repository.save(game_status_repository.game_status_repository.game_status, player_status_repository.player_status_repository.player_status, round_status_repository.round_status_repository.round_status)

    def log(self):
        pass