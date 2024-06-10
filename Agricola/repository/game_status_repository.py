"""
게임 상태 저장소
"""
import entity.game_status as game_status


class GameStatusRepository:
    def __init__(self):
        self.game_status = game_status.GameStatus()


game_status_repository = GameStatusRepository()
