from command import Command
import repository.game_status_repository as  game_status_repository
import repository.round_status_repository as round_repo


def findNextRoundPlayer(nowPlayer, roundPlayer):
    nextPlayer = (nowPlayer + 1) % len(roundPlayer)
    while not roundPlayer[nextPlayer]:
        nextPlayer = (nextPlayer + 1) % len(roundPlayer)
    return nextPlayer


class RoundPlayer(Command):
    def __init__(self):
        self.nowRoundPlayers = [True, True, True, True]
        self.round_remain_worker = round_repo.round_status_repository.round_status.remain_workers
        self.game_status = game_status_repository.game_status_repository.game_status

    def execute(self):
        nowPlayer = game_status_repository.game_status_repository.game_status.now_turn_player
        self.game_status.now_turn_player = self.game_status.next_turn_player

    def log(self):
        pass
