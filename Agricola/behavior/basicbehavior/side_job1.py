"""
효율 교습
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from Agricola_Back.Agricola.behavior.basebehavior.buy_job_card_1 import BuyJobCard1
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.playable_sub_job_listup import PlayableJobCardListup
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.command import Command
from Agricola_Back.Agricola.entity.basic_behavior_type import BasicBehaviorType
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.player_status_repository as player_repo
import Agricola_Back.Agricola.repository.round_status_repository as round_repo


class SideJob1(BehaviorInterface):

    def __init__(self):
        self.log_text = ""
        player = game_status_repository.game_status_repository.game_status.now_turn_player
        self.player = player
        self.player_resource = player_repo.player_status_repository.player_status[player].resource
        self.player_ownCard = player_repo.player_status_repository.player_status[player].own_card
        self.is_filled = round_repo.round_status_repository.round_status.put_basic[BasicBehaviorType.SIDE_JOB1.value]

    def can_play(self):
        if self.player_ownCard.hand_job_card and ((not self.player_ownCard.put_job_card) or self.player_resource.food >= 1):
            self.log_text = "직업을 낼 수 있습니다."
            return True
        else:
            self.log_text = "비용이 없어 행동이 불가능합니다"
            return False

    def execute(self):
        return [ UseWorker]

    def log(self):
        return self.log_text
