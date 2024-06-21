from command import Command
import repository.player_status_repository as player_status_repository
import repository.round_status_repository as round_status_repository


class SetRoundWorkerResource(Command):
    def execute(self):
        round_status = round_status_repository.round_status_repository.round_status
        for i in range(4):
            round_status.set_remain_workers(i, player_status_repository.player_status_repository.player_status[i].worker)

    def log(self):
        return "일꾼이 할당되었습니다."