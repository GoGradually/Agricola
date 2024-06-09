"""
플레이어 상태 저장소
"""
from multiprocessing.managers import BaseManager

from entity.player_status import PlayerStatus


class PlayerStatusRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PlayerStatusRepository, cls).__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def get_player_status(self):
        return self._player_status
    def _init(self):
        self._player_status = [PlayerStatus() for i in range(5)]


__all__ = ['player_status_repository']

class PlayerStatusRepositoryManager(BaseManager):
    pass

PlayerStatusRepositoryManager.register('PlayerStatusRepository', PlayerStatusRepository)
