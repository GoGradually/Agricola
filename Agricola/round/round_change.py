from command import Command
import repository.game_status_repository as game_status_repository


class RoundChange(Command):
    def execute(self):
        game_status_repository.game_status_repository.game_status.set_now_round(game_status_repository.game_status_repository.game_status.now_round + 1)

    def log(self):
        pass