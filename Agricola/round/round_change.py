import repository.game_status_repository as game_repo


class RoundChange():
    def execute(self):
        game_repo.game_status_repository.game_status.set_now_round(game_repo.game_status_repository.game_status.now_round + 1)
        print(f"현재 라운드는 {game_repo.game_status_repository.game_status.now_round} 입니다.")
    def log(self):
        pass