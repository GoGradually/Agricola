from command import Command




class SetRoundWorkerResource(Command):
    def execute(self):
        round_status = round_status_repository.round_status
        for i in range(4):
            round_status.set_remain_workers(i, player_status_repository.get_player_status()[i].worker)

    def log(self):
        return "일꾼이 할당되었습니다."