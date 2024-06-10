from command import Command
import repository.game_status_repository as  game_status_repository
import repository.round_status_repository as round_repo


class CanEnterRoundBehavior(Command):
    def __init__(self, round_index):
        self.log_text = ""
        self.round = round_index

    def execute(self):
        behavior = game_status_repository.game_status_repository.game_status.round_card_command_factory(self.round)
        if round_repo.round_status_repository.round_status.put_round[self.round] == -1 and \
                behavior.can_play():
            self.log_text = "행동에 진입 가능합니다."
            return True
        else:
            self.log_text = "행동에 진입할 수 없습니다."
            return False

    def log(self):
        return self.log_text
