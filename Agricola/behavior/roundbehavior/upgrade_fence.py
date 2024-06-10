"""
집 한번 고친 후에 울타리 치기 라운드 행동
:param: 플레이어 번호, 바꾸고자 하는 농장 상태
:return: 실행 결과.
:rtype: bool
"""
from Agricola_Back.Agricola.behavior.basebehavior.construct_fence import ConstructFence
from Agricola_Back.Agricola.behavior.basebehavior.house_upgrade import HouseUpgrade
from Agricola_Back.Agricola.behavior.behavior_interface import BehaviorInterface
from Agricola_Back.Agricola.behavior.unitbehavior.use_worker import UseWorker
from Agricola_Back.Agricola.command import Command
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.round_status_repository as round_repo


class UpgradeFence(BehaviorInterface):

    def can_play(self):
        return HouseUpgrade().can_play()

    def execute(self):
        return [HouseUpgrade, ConstructFence, UseWorker]

    def log(self):
        pass
