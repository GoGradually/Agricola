from command import Command
import repository.game_status_repository as game_status_repository


class HarvestChangeTurn(Command):
    def execute(self):
        game_status_repository.game_status_repository.game_status.now_turn_player = game_status_repository.game_status_repository.game_status.next_turn_player

    def log(self):
        pass