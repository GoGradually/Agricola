"""
undo point 를 저장하는 커맨드
"""
from command import Command



from repository.undo_repository import undo_repository


class SaveUndoPoint(Command):
    def execute(self):
        undo_repository.save(game_status_repository.get_game_status(), player_status_repository.get_player_status(), round_status_repository.round_status)

    def log(self):
        pass