from command import Command
import repository.player_status_repository as player_repo
import repository.round_status_repository as round_repo


class SetRoundWorkerResource(Command):
    def execute(self):
        round_status = round_repo.round_status_repository.round_status
        for i in range(4):
            round_status.set_remain_workers(i, player_repo.player_status_repository.player_status[i].worker)

    def log(self):
        return "일꾼이 할당되었습니다."