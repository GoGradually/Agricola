from command import Command



class CheckHarvestTurnRemain(Command):
    def execute(self):
        if game_status_repository.get_game_status().next_turn_player == 4:
            game_status_repository.get_game_status().next_turn_player = -1

    def log(self):
        pass
