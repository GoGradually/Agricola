import repository.game_status_repository as game_repo
import repository.round_status_repository as round_repo


class PredictTurnTurnStart():
    def execute(self):
        for i in range(1, 5):
            if round_repo.round_status_repository.round_status.remain_workers[(game_repo.game_status_repository.game_status.now_turn_player + i)%4] > 0:
                game_repo.game_status_repository.game_status.set_next_turn_player((game_repo.game_status_repository.game_status.now_turn_player + i)%4)
                return game_repo.game_status_repository.game_status.next_turn_player
        game_repo.game_status_repository.game_status.set_next_turn_player(-1)
        return -1

    def log(self):
        pass