"""
턴을 바꾸는 커맨드
"""
import repository.game_status_repository as game_repo


class ChangeTurn():
    def execute(self):
        game_repo.game_status_repository.game_status.set_now_turn_player(game_repo.game_status_repository.game_status.next_turn_player)
        game_repo.game_status_repository.game_status.acted = False
        return game_repo.game_status_repository.game_status.now_turn_player

    def log(self):
        pass