from command import Command



class HarvestPredictTurnRoundStart(Command):
    def execute(self):
        game_status_repository.get_game_status().set_next_turn_player(0)

    def log(self):
        pass
