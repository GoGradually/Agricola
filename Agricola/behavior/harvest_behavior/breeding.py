"""
동물 번식 커맨드. 맵 반환
이후 동물 배치 기초 행동으로 동물 배치하여 마무리해야 함? 동물 번식을 반드시 마무리 지어야 턴을 넘길 수 있는데
"""
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.command import Command
from Agricola_Back.Agricola.entity.animal_type import AnimalType
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.player_status_repository as player_repo


class Breeding(BehaviorInterface):
    def execute(self):
        ret = {}
        if player_repo.player_status_repository.player_status[ \
                game_status_repository.game_status_repository.game_status.now_turn_player].farm.get_cow_count() >= 2:
            ret[AnimalType.COW] = 1
        if player_repo.player_status_repository.player_status[ \
                game_status_repository.game_status_repository.game_status.now_turn_player].farm.get_sheep_count() >= 2:
            ret[AnimalType.SHEEP] = 1
        if player_repo.player_status_repository.player_status[ \
                game_status_repository.game_status_repository.game_status.now_turn_player].farm.get_pig_count() >= 2:
            ret[AnimalType.PIG] = 1
        return ret

    def log(self):
        pass
