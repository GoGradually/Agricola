"""
흙 채굴장
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_status_repository
import repository.round_status_repository as round_status_repository


# Todo

class Dirt1(BehaviorInterface):
    def __init__(self):
        self.log_text = ""
        player = game_status_repository.game_status_repository.game_status.now_turn_player
        self.game_status = game_status_repository.game_status_repository.game_status
        self.player_resource = player_status_repository.player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status_repository.round_status.put_basic[BasicBehaviorType.DIRT1.value]

    def execute(self):
        self.player_resource.set_dirt(
            self.player_resource.dirt + self.game_status.basic_resource[BasicBehaviorType.DIRT1.value])
        self.log_text = f"흙 {self.game_status.basic_resource[BasicBehaviorType.DIRT1.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(BasicBehaviorType.DIRT1.value, 0)
        return [UseWorker]

    def log(self):
        return self.log_text

