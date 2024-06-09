from command import Command




class UseWorker(Command):
    def __init__(self, is_round_active, index):
        self.is_round_active = is_round_active
        self.index = index

    def execute(self):
        player = game_status_repository.get_game_status().now_turn_player
        game_status_repository.get_game_status().acted = True
        round_status_repository.round_status.remain_workers[player] -= 1
        if self.is_round_active:
            round_status_repository.round_status.set_put_round(self.index, game_status_repository.get_game_status().now_turn_player)
        else:
            round_status_repository.round_status.set_put_basic(self.index, game_status_repository.get_game_status().now_turn_player)


    def log(self):
        pass

    def __init__(self):
        pass
