"""
게임 상태 저장소
"""
import multiprocessing
from multiprocessing import Manager
from multiprocessing.managers import BaseManager

from entity.game_status import GameStatus

class GameStatusRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameStatusRepository, cls).__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._game_status = GameStatus()

    def get_game_status(self):
        return self._game_status

    def __str__(self):
        return f"GameStatusRepository(id={id(self)}, game_status_id={id(self.get_game_status())})"

__all__ = ['game_status_repository']

class GameStatusRepositoryManager(BaseManager):
    pass

GameStatusRepositoryManager.register('GameStatusRepository', GameStatusRepository)
if '__main__' == __name__:
    game_status_repository = GameStatusRepository()
    print("모듈 임포트됨")
    print(game_status_repository)