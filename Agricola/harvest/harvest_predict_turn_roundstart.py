from command import Command
import repository.game_status_repository as game_status_repository


class HarvestPredictTurnRoundStart(Command):
    def execute(self):
        game_status_repository.game_status_repository.game_status.set_next_turn_player(0)

    def log(self):
        pass
