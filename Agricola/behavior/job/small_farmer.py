"""
소규모 농부 직업 카드
"""
from behavior.job.job_interface import JobInterface
from entity import card_type
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_status_repository


class SmallFarmer(JobInterface):
    def __init__(self, input_behavior):
        self.input_behavior = input_behavior
        self.card_type = card_type.CardType.job
    """
    사용 가능 여부를 반환하는 메소드
    :param:
    :return: 현재 해당 카드 사용 가능 여부
    :rtype: bool
    """
    def canUse(self):
        farm = player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].farm
        house_count = farm.get_house_count()
        current_player_cards = player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].card.put_job_card
        small_farmer_card_present = any(isinstance(card, SmallFarmer) for card in current_player_cards)

        if house_count >= 2 and small_farmer_card_present:
            return True
        else:
            return False
        self.log_text = "소규모 농부 사용"

    """
    카드 사용 메소드
    :param: 
    :return: 사용 성공 여부
    :rtype: bool
    """
    def execute(self):
        pass

    """
    로그 반환
    :param:
    :return: 가장 최근에 저장된 로그 문자열 반환
    :rtype: str
    """
    def log(self):
        return self.log_text

    """
    카드 내려놓기 메소드
    :return: 카드 내려놓기 성공 여부 반환
    :rtype: bool
    """
    def putDown(self):
        current_player = player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player]
        current_player.card.hand_job_card.remove(self)
        current_player.card.put_job_card.append(self)