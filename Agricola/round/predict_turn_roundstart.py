from command import Command




class PredictTurnRoundStart(Command):
    def execute(self):
        for i in range(4):
            if player_status_repository.get_player_status()[i].resource.first_turn:
                game_status_repository.get_game_status().next_turn_player = i

    def log(self):
        pass