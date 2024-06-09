"""
나무 누적 2개 기본 행동 구현
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from entity.basic_behavior_type import BasicBehaviorType





class Wood2(BehaviorInterface):
    def __init__(self):
        self.log_text = ""
        self.game_status = game_status_repository.get_game_status()
        player = game_status_repository.get_game_status().now_turn_player
        self.player_resource = player_status_repository.get_player_status()[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.WOOD2.value]

    def can_play(self):
        return True

    def execute(self):
        self.player_resource.set_wood(
            self.player_resource.wood + self.get_game_status().basic_resource[BasicBehaviorType.WOOD2.value])
        self.log_text = f"나무 {self.get_game_status().basic_resource[BasicBehaviorType.WOOD2.value]}개를 획득하였습니다."
        self.get_game_status().set_basic_resource(BasicBehaviorType.WOOD2.value, 0)
        return [UseWorker]

    def log(self):
        return self.log_text
