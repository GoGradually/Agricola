from command import Command
import repository.game_status_repository as  game_status_repository
import repository.player_status_repository as player_repo
import repository.round_status_repository as round_repo
from repository.undo_repository import undo_repository


class HarvestSaveUndoPoint(Command):
    def execute(self):
        undo_repository.save(game_status_repository.game_status_repository.game_status, player_status_repository.player_status,round_repo.round_status_repository.round_status)

    def log(self):
        pass