from collections import deque


def animal_move_validation(field_status, animal_type, position):
    chk_already = check_already_placed(field_status, position)
    chk_same_type = check_same_type(field_status, animal_type, position)
    combined_status = chk_already[0] and chk_same_type[0]
    combined_log = [chk_already[1], chk_same_type[1]]
    return (combined_status, combined_log)


def check_already_placed(field_status, position):
    log_text = ""
    from entity.field_type import FieldType
    if field_status[position[0] * 2 + 1][position[1] * 2 + 1].field_type != FieldType.NONE_FIELD \
            and field_status[position[0] * 2 + 1][position[1] * 2 + 1].field_type != FieldType.CAGE:
        log_text = "다른 구조물 위에 동물을 놓을 수 없습니다."
        return (False, log_text)
    return (True, log_text)


def check_same_type(field_status, animal_type, position):
    check = [[0 for _ in range(11)] for _ in range(7)]
    queue = deque()
    log_text = ""
    from entity.animal_type import AnimalType
    from entity.farm.none_field import NoneField
    if field_status[position[0] * 2 + 1][position[1] * 2 + 1].kind != AnimalType.NONE \
            and field_status[position[0] * 2 + 1][position[1] * 2 + 1].kind != animal_type:
        log_text = "한 울타리 안에는 서로 다른 종류의 동물이 존재할 수 없습니다."
        return (False, log_text)

    if field_status[position[0] * 2 + 1][position[1] * 2 + 1].barn and isinstance(
            field_status[position[0] * 2 + 1][position[1] * 2 + 1], NoneField):
        return (True, log_text)
    check[position[0] * 2 + 1][position[1] * 2 + 1] = 1
    queue.append((position[0] * 2 + 1, position[1] * 2 + 1))
    while queue:
        x, y = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]
            r = p + dx[i]
            s = q + dy[i]
            from entity.field_type import FieldType
            if 7 > r >= 0 and 0 <= s < 11 \
                    and check[r][s] == 0 and field_status[p][q].field_type != FieldType.FENCE \
                    and not (field_status[r][s].barn and isinstance(field_status[r][s], NoneField)):
                if field_status[r][s].kind != AnimalType.NONE \
                        and field_status[r][s].kind != animal_type:
                    log_text = "한 울타리 안에는 서로 다른 종류의 동물이 존재할 수 없습니다."
                    return (False, log_text)
                check[r][s] = 1
                queue.append((r, s))
    return (True, log_text)
