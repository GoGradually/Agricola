"""
턴이 남아있는지 체크하는 커맨드
"""
from command import Command




class CheckTurnRemain(Command):
    def execute(self):
        for i in range(4):
            if round_status_repository.round_status.remain_workers[i] > 0:
                return
        game_status_repository.get_game_status().set_next_turn_player(-1)

    def log(self):
        pass