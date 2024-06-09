from command import Command



class HarvestChangeTurn(Command):
    def execute(self):
        game_status_repository.get_game_status().now_turn_player = game_status_repository.get_game_status().next_turn_player

    def log(self):
        pass