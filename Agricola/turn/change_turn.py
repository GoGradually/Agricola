"""
턴을 바꾸는 커맨드
"""
from command import Command



class ChangeTurn(Command):
    def execute(self):
        game_status = game_status_repository.get_game_status()
        game_status.set_now_turn_player(game_status.next_turn_player)
        game_status.acted = False
        return game_status.now_turn_player

    def log(self):
        pass