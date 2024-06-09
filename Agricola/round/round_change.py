from command import Command



class RoundChange(Command):
    def execute(self):
        game_status_repository.get_game_status().set_now_round(game_status_repository.get_game_status().now_round + 1)

    def log(self):
        pass