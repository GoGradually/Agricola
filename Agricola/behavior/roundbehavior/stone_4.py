"""
채석장 라운드 행동 - 4주기
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.command import Command
from Agricola_Back.Agricola.entity.round_behavior_type import RoundBehaviorType
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.player_status_repository as player_repo
import Agricola_Back.Agricola.repository.round_status_repository as round_repo



class Stone4(BehaviorInterface):
    def __init__(self,game_status,player_status,round_status, player):
        self.log_text = ""
        self.game_status = game_status_repository.game_status_repository.game_status
        self.player_resource = player_repo.player_status_repository.player_status[player].resource

    def can_play(self):
        return True

    def execute(self):
        stone2_card_index = game_status_repository.game_status_repository.game_status.get_stone2_card_index()
        self.player_resource.set_stone(
            self.player_resource.stone + self.game_status.round_resource[stone2_card_index])
        self.log_text = f"돌 {self.game_status.round_resource[stone2_card_index]}개를 획득하였습니다."
        self.game_status.set_round_resource(stone2_card_index, 0)
        return [UseWorker]

    def log(self):
        return self.log_text
