"""
가족 먹여살리기
"""
from command import Command




class FeedingFamily(Command):
    def execute(self):
        need = player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].worker * 3
        need += player_status_repository.get_player_status()[game_status_repository.get_game_status().next_turn_player].baby
        player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.food -= need
        if player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.food < 0:
            beg = -player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.food
            player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.food = 0
            player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.beg_token += beg
            return beg
        return 0

    def log(self):
        pass
