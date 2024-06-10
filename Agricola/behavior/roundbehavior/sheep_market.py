"""
양 시장 라운드 행동
:param: 플레이어 번호
:return: 획득한 동물이 담긴 큐
:rtype: deque
"""
from Agricola_Back.Agricola.behavior.basebehavior.gain_animal import GainAnimal
from Agricola_Back.Agricola.behavior.basebehavior.place_animal import PlaceAnimal
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.command import Command
from Agricola_Back.Agricola.entity.round_behavior_type import RoundBehaviorType
from Agricola_Back.Agricola.entity.animal_type import AnimalType


class SheepMarket(BehaviorInterface):
    def __init__(self,game_status,player_status,round_status):
        self.log_text = ""
        self.game_status = game_status

    def can_play(self):
        return True

    def execute(self):
        sheep_card_index = self.game_status.get_sheep_card_index()
        self.log_text = f"양 {self.game_status.round_resource[sheep_card_index]}마리를 획득하였습니다."
        ret = [PlaceAnimal,
               GainAnimal(AnimalType.SHEEP, self.game_status.round_resource[sheep_card_index]), UseWorker]
        self.game_status.set_round_resource(sheep_card_index, 0)
        return ret

    def log(self):
        return self.log_text
