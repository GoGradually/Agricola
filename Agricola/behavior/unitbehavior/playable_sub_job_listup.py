"""
제출 가능한 직업 카드 리스트업 함수
:param: 플레이어 번호
:return: 제출 가능한 직업 카드 리스트 반환
:rtype: list<card_name>
"""
from command import Command
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_status_repository


class PlayableJobCardListup(Command):
    def __init__(self):
        self.log_text = ""
        player = game_status_repository.game_status_repository.game_status
        self.jobList = self.player_ownCard = player_status_repository.player_status_repository.player_status[player].own_card.hand_job_card

    def execute(self):
        self.log_text = "구매 가능한 직업을 확인했습니다"
        return self.jobList

    def log(self):
        return self.log_text
