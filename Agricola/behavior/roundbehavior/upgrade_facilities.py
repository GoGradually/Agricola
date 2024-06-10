"""
집 고친 후에 주요 설비/보조 설비 1개 놓기 라운드 행동
:param: 플레이어 번호, 선택하고자 하는 설비 카드
:return: 실행 결과.
:rtype: bool
"""
from Agricola_Back.Agricola.behavior.basebehavior.buy_main_card import BuyMainCard
from Agricola_Back.Agricola.behavior.basebehavior.buy_sub_card import BuySubCard
from Agricola_Back.Agricola.behavior.basebehavior.house_upgrade import HouseUpgrade
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.playable_sub_facility_listup import PlayableSubCardListup
from Agricola_Back.Agricola.behavior.unitbehavior.purchasable_main_facility_listup import PurchasableMainCardListup
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.command import Command
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.round_status_repository as round_repo


class UpgradeFacilities(BehaviorInterface):
    def __init__(self,game_status,player_status,round_status):
        self.log_text = ""

    def can_play(self):
        return HouseUpgrade().can_play()

    def execute(self):
        ret = [HouseUpgrade, UseWorker]
        return ret

    def log(self):
        return self.log_text
