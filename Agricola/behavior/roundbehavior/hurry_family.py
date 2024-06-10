"""
급한 가족 늘리기 라운드 행동
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


# Todo

class HurryFamily(BehaviorInterface):

    def __init__(self,game_status,player_status,round_status, player):
        self.log_text = ""
        self.player_status = player_repo.player_status_repository.player_status[player]
        self.is_filled = round_repo.round_status_repository.round_status.put_basic[RoundBehaviorType.HURRY_FAMILY.value]

    def can_play(self):
        if self.player_status.baby + self.player_status.worker == 5:
            self.log_text = "더 이상 가족을 늘릴 수 없습니다"
            return False
        else:
            return True

    def execute(self):
        self.player_status.set_baby(player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].baby + 1)
        self.log_text = "급한 가족 늘리기를 성공했습니다"
        return [UseWorker]

    def log(self):
        return self.log_text
