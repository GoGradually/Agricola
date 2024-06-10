"""
라운드 상태 저장소
"""
import entity.round_status as round_status


class RoundStatusRepository:
    def __init__(self):
        self.round_status = round_status.RoundStatus()


round_status_repository = RoundStatusRepository()