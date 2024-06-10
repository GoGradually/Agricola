"""
창고 관리인 직업 카드
"""
from Agricola_Back.Agricola.behavior.basicbehavior.resource_market import ResourceMarket
from Agricola_Back.Agricola.behavior.job.job_interface import JobInterface
from entity import card_type
import Agricola_Back.Agricola.repository.game_status_repository as  game_status_repository
import Agricola_Back.Agricola.repository.player_status_repository as player_repo


class WarehouseManager(JobInterface):
    def __init__(self, input_behavior):
        self.log_text = None
        self.input_behavior = input_behavior
        self.card_type = card_type.CardType.job
    """
    사용 가능 여부를 반환하는 메소드
    :param:
    :return: 현재 해당 카드 사용 가능 여부
    :rtype: bool
    """
    def canUse(self):
        current_player_cards = player_repo.player_status_repository.player_status[
            game_status_repository.game_status_repository.game_status.now_turn_player].card.put_job_card
        warehouse_manager_card_present = any(isinstance(card, WarehouseManager) for card in current_player_cards)

        if isinstance(self.input_behavior, ResourceMarket) and warehouse_manager_card_present:
            return True
        else:
            return False

    """
    카드 사용 메소드
    :param: 
    :return: 사용 성공 여부
    :rtype: bool
    """
    def execute(self, add_dirt: bool):
        current_player = player_repo.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player]

        if add_dirt:
            current_player.resource.set_dirt(current_player.resource.dirt + 1)
            self.log_text = "창고 관리인 사용: 흙 추가"
        else:
            current_player.resource.set_grain(current_player.resource.grain + 1)
            self.log_text = "창고 관리인 사용: 곡식 추가"
        return True

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
        current_player = player_repo.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player]
        current_player.card.hand_job_card.remove(self)
        current_player.card.put_job_card.append(self)
        self.log_text = "창고 관리인 내려 놓음"