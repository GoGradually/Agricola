"""
소 시장 라운드 행동
:param:
:return: 획득한 동물이 담긴 맵과 이후 수행할 행동
:rtype: 행동 리스트
"""
from behavior.basebehavior.gain_animal import GainAnimal
from behavior.basebehavior.place_animal import PlaceAnimal
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from entity.round_behavior_type import RoundBehaviorType



from entity.animal_type import AnimalType


class CowMarket(BehaviorInterface):
    def __init__(self):
        player = game_status_repository.get_game_status().now_turn_player
        self.log_text = ""
        self.game_status =  game_status_repository.get_game_status()
        self.player_resource = player_status_repository.get_player_status()[player].resource

    def execute(self):
        cow_card_index = game_status_repository.get_game_status().get_cow_card_index()
        self.log_text = f"소 {self.get_game_status().round_resource[cow_card_index]}마리를 획득하였습니다."
        ret = [PlaceAnimal, GainAnimal(AnimalType.COW, self.get_game_status().round_resource[cow_card_index]), UseWorker]
        self.get_game_status().set_round_resource(cow_card_index, 0)
        return ret

    def log(self):
        return self.log_text
