"""
undo 를 위한 현재 상태 저장소
"""
from entity.get_game_status() import GameStatus
from entity.player_status import PlayerStatus
from entity.round_status import RoundStatus

import copy



class UndoRepository:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UndoRepository, cls).__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance
    def _init(self):
        self.round_status = None
        self.player_status = None
        self.game_status = None
    def __init__(self):
        self.round_status = None
        self.player_status = None
        self.game_status = None

    def undo(self):
        game_status_repository._game_status = self.game_status
        player_status_repository._player_status = self.player_status
        round_status_repository._round_status = self.round_status
        self.save(self.game_status, self.player_status, self.round_status)

    def save(self, game_status: GameStatus, player_status: PlayerStatus, round_status: RoundStatus):
        self.game_status = copy.deepcopy(game_status)
        self.player_status = copy.deepcopy(player_status)
        self.round_status = copy.deepcopy(round_status)
