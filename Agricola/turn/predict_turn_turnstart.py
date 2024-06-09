from command import Command




class PredictTurnTurnStart(Command):
    def execute(self):
        for i in range(1, 5):
            if round_status_repository.round_status.remain_workers[(game_status_repository.get_game_status().now_turn_player + i)%4] > 0:
                game_status_repository.get_game_status().set_next_turn_player((game_status_repository.get_game_status().now_turn_player + i)%4)

    def log(self):
        pass