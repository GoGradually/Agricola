"""
라운드 상태 저장소
"""
from multiprocessing.managers import BaseManager

from entity.round_status import RoundStatus


class RoundStatusRepository:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RoundStatusRepository, cls).__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance
    def get_round_status(self):
        return self._round_status
    def _init(self):
        self._round_status = RoundStatus()


__all__ = ['round_status_repository']

class RoundStatusRepositoryManager(BaseManager):
    pass

RoundStatusRepositoryManager.register('RoundStatusRepository', RoundStatusRepository)