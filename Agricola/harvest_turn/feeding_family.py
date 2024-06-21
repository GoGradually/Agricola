"""
가족 먹여살리기
"""
from command import Command
import repository.game_status_repository as game_status_repository
import repository.player_status_repository as player_status_repository


class FeedingFamily(Command):
    def execute(self):
        need = player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].worker * 3
        need += player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.next_turn_player].baby
        player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].resource.food -= need
        if player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].resource.food < 0:
            beg = -player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].resource.food
            player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].resource.food = 0
            player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].resource.beg_token += beg
            return beg
        return 0

    def log(self):
        pass
