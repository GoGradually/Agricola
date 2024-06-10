from command import Command
import repository.game_status_repository as  game_status_repository


class CheckHarvestTurnRemain(Command):
    def execute(self):
        if game_status_repository.game_status_repository.game_status.next_turn_player == 4:
            game_status_repository.game_status_repository.game_status.next_turn_player = -1

    def log(self):
        pass
