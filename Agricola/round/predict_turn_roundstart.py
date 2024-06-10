from command import Command
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_repo


class PredictTurnRoundStart(Command):
    def execute(self):
        for i in range(4):
            if player_repo.player_status_repository.player_status[i].resource.first_turn:
                game_status_repository.game_status_repository.game_status.next_turn_player = i

    def log(self):
        pass