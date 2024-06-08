from copy import deepcopy


def move_animal(field_status):
    changed_field = deepcopy(field_status)
    log_text = ""
    response = chk_animal_position(changed_field)
    if response[0]:
        from repository.player_status_repository import player_status_repository
        from repository.game_status_repository import game_status_repository
        player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player].farm.field = field_status
    return response


def chk_animal_position(field_status):
    log_text = ""
    for i, items in enumerate(field_status):
        for j, item in enumerate(items):
            from entity.field_type import FieldType
            if item.field_type == FieldType.CAGE or item.field_type == FieldType.NONE_FIELD:
                if item.count >= item.maximum:
                    log_text = f"({i}, {j})위치에 동물이 너무 많습니다."
                    return (False, log_text)
                elif item.count < 0:
                    log_text = f"({i}, {j})위치의 동물의 수가 음수입니다."
                    return (False, log_text)
    return (True, log_text)
