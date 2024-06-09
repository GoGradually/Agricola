from command import Command

from entity.card_factory import basic_card_command_factory

from Agricola.Agricola.repository.round_status_repository import RoundStatusRepository, RoundStatusRepositoryManager


class CanEnterBaseBehavior(Command):
    def __init__(self, behavior_index, round_status):
        self.log_text = ""
        self.round_status = round_status
        self.behavior_index = behavior_index

    def execute(self):
        behavior = basic_card_command_factory(self.behavior_index)
        if self.round_status.put_basic[self.behavior_index] == -1 and \
                behavior().can_play():
            self.log_text = "행동이 진입가능합니다."
            return True
        else:
            self.log_text = "행동을 진입할 수 없습니다"
            return False

    def log(self):
        return self.log_text
