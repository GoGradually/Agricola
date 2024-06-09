"""
작물 수확 커맨드
"""
from command import Command
from entity.crop_type import CropType
from entity.field_type import FieldType




class Harvesting(Command):
    def execute(self):
        for row in player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].farm.field:
            for field in row:
                if field.field_type == FieldType.ARABLE and field.count > 0:
                    field.count -= 1
                    if field.kind == CropType.GRAIN:
                        player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.grain += 1
                    if field.kind == CropType.VEGETABLE:
                        player_status_repository.get_player_status()[game_status_repository.get_game_status().now_turn_player].resource.vegetable += 1
                    if field.count == 0:
                        field.kind = CropType.NONE

    def log(self):
        pass