"""
곡식 종자 기본 행동
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.command import Command
from Agricola_Back.Agricola.entity.basic_behavior_type import BasicBehaviorType
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.player_status_repository as player_repo
import Agricola_Back.Agricola.repository.round_status_repository as round_repo


class Seed(BehaviorInterface):
    def __init__(self):
        self.log_text = ""
        self.game_status = game_status_repository.game_status_repository.game_status
        player = game_status_repository.game_status_repository.game_status.now_turn_player
        self.player_resource = player_repo.player_status_repository.player_status[player].resource
        self.is_filled = round_repo.round_status_repository.round_status.put_basic[BasicBehaviorType.SEED.value]

    def can_play(self):
        return True

    def execute(self):
        self.player_resource.set_grain(
            self.player_resource.grain + self.game_status.basic_resource[BasicBehaviorType.SEED.value])
        self.log_text = f"곡식 {self.game_status.basic_resource[BasicBehaviorType.SEED.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(BasicBehaviorType.SEED.value, 1)
        return [UseWorker]

    def log(self):
        return self.log_text
