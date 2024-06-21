"""
제출 가능한 보조 설비 리스트 업 함수
:param: 플레이어 번호
:return: 제출 가능한 보조 설비 리스트 반환
:rtype: list<card_name>
"""
from command import Command
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_status_repository


class PlayableSubCardListup(Command):

    def __init__(self):
        self.log_text = ""
        player = game_status_repository.game_status_repository.game_status.now_turn_player
        self.subFacilityList = self.player_ownCard = player_status_repository.player_status_repository.player_status[player].own_card.hand_sub_card

    def execute(self):
        can_use_sub_facility_list = [subFac for subFac in self.subFacilityList if subFac.canPutDown()]
        self.log_text = ""
        return can_use_sub_facility_list

    def log(self):
        return self.log_text
