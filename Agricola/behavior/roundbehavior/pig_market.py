"""
돼지 시장 라운드 행동
:param:
:return: 획득한 동물이 담긴 맵과 이후 수행할 행동
:rtype: 행동 리스트
"""
from Agricola_Back.Agricola.behavior.basebehavior.gain_animal import GainAnimal
from Agricola_Back.Agricola.behavior.basebehavior.place_animal import PlaceAnimal
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.entity.round_behavior_type import RoundBehaviorType
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
from Agricola_Back.Agricola.entity.animal_type import AnimalType


class PigMarket(BehaviorInterface):
    def __init__(self,game_status,player_status,round_status):
        self.log_text = ""
        self.game_status = game_status_repository.game_status_repository.game_status

    def can_play(self):
        return True

    def execute(self):
        pig_card_index = game_status_repository.game_status_repository.game_status.get_pig_card_index()
        self.log_text = f"돼지 {self.game_status.round_resource[pig_card_index]}마리를 획득하였습니다."
        ret = [PlaceAnimal, GainAnimal(AnimalType.PIG, self.game_status.round_resource[pig_card_index]), UseWorker]
        self.game_status.set_round_resource(pig_card_index, 0)
        return ret

    def log(self):
        return self.log_text
