"""
자원 시장 기본 행동
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from entity.basic_behavior_type import BasicBehaviorType





class ResourceMarket(BehaviorInterface):
    def __init__(self):
        self.log_text = ""
        self.game_status =  game_status_repository.get_game_status()
        player = game_status_repository.get_game_status().now_turn_player
        self.player_resource = player_status_repository.get_player_status()[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.MARKET.value]

    def can_play(self):
        return True

    def execute(self):
        self.player_resource.set_food(
            self.player_resource.food + self.get_game_status().basic_resource[BasicBehaviorType.MARKET.value])
        self.player_resource.set_stone(
            self.player_resource.stone + self.get_game_status().basic_resource[BasicBehaviorType.MARKET.value])
        self.player_resource.set_reed(
            self.player_resource.reed + self.get_game_status().basic_resource[BasicBehaviorType.MARKET.value])
        self.log_text = f"갈대, 흙, 음식 {self.get_game_status().basic_resource[BasicBehaviorType.MARKET.value]}개를 획득하였습니다."
        self.get_game_status().set_basic_resource(BasicBehaviorType.MARKET.value, 1)
        return [UseWorker]

    def log(self):
        return self.log_text
