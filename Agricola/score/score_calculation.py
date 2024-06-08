from command import Command


class ScoreCalculation(Command):
    def __init__(self, playerNum):  # playerNum=>[0,1,2,3] 점수계산하고싶은 플레이어 번호 매개변수
        # 추가 저장없이 한번에 모든 플레이 점수 계산하고싶으면 매개변수없애고 execute 함수 내용 따로 빼놓고 호출해서 인덱스로
        # 점수 가져오면 될듯??
        self.log_text = None
        from repository.player_status_repository import player_status_repository  # 순환참조 오류 회피
        self.player_status_list = player_status_repository.player_status
        self.playerNum = playerNum

    def execute(self):
        score = 0
        arable_score = lambda value: 4 if value >= 5 else -1 if value <= 1 else value - 1
        score += arable_score(self.player_status_list[self.playerNum].farm.get_arable_count())  # 밭

        cage_score = None  # 우리 갯수 가져오는 함수 추가필요
        score += cage_score  # 우리 갯수 계산 0개 -> -1 1개 -> 1 2개 -> 2 3개-> 3 4개이상 -> 4
        # 3x3 9칸짜리 우리여도 우리 1개로 계산함

        grain_score = lambda \
                value: 4 if value >= 8 else 3 if value >= 6 else 2 if value >= 4 else 1 if value >= 1 else -1
        score += grain_score(self.player_status_list[self.playerNum].resource.grain)  # 곡식

        vegetable_score = lambda \
                value: 4 if value >= 4 else -1 if value == 0 else value
        score += vegetable_score(self.player_status_list[self.playerNum].resource.vegetable)  # 채소

        sheep_score = lambda \
                value: 4 if value >= 8 else 3 if value >= 6 else 2 if value >= 4 else 1 if value >= 1 else -1
        score += sheep_score(self.player_status_list[self.playerNum].farm.get_sheep_count())  # 양

        pig_score = lambda \
                value: 4 if value >= 7 else 3 if value >= 5 else 2 if value >= 3 else 1 if value >= 1 else -1
        score += pig_score(self.player_status_list[self.playerNum].farm.get_pig_count())  # 멧돼지

        cow_score = lambda \
                value: 4 if value >= 6 else 3 if value >= 4 else 2 if value >= 2 else 1 if value == 1 else -1
        score += cow_score(self.player_status_list[self.playerNum].farm.get_cow_count())  # 소

        score -= self.player_status_list[self.playerNum].farm.get_none_field_count()  # 사용하지 않는 빈칸당 감점
        # 빈칸을 none_field가 아니라 cage로 처리한다했었나??? << 맞을시 get count 수정바람

        from entity.house_type import HouseType
        houseType = self.player_status_list[self.playerNum].farm.house_status
        house_score = lambda value: self.player_status_list[
            self.playerNum].farm.get_house_count() if houseType == HouseType.DIRT \
            else self.player_status_list[self.playerNum].farm.get_house_count() * 2 if houseType == houseType.STONE \
            else 0
        score += house_score  # 집 등급 따라 점수

        score += (self.player_status_list[self.playerNum].farm.get_barn_with_fence_count())
        # 울타리 안 외양간
        # 외양간 갯수세는 get barn에서 추가로 울타리 안 확인하는 with fence 함수 새로 만듬

        score += (self.player_status_list[self.playerNum].worker + self.player_status_list[self.playerNum].baby) * 3
        # 가족 구성원당 3점

        score -= self.player_status_list[self.playerNum].resource.beg_token * 3
        # 감점 토큰(-3)

        score += sum(card.score for card in self.player_status_list[self.playerNum].card.put_sub_card)
        score += sum(card.score for card in self.player_status_list[self.playerNum].card.put_main_card)
        # 설비 기본 점수
        # 기본 점수를 가질수있는 주요 설비와 보조 설비(직업은 불가능)에 대해 init 변수 self.score 추가

        scoreSubCard = [card for card in self.player_status_list[self.playerNum].card.put_sub_card if card.canUse()]
        # 점수 계산때 발동하는 보조 설비카드를 찾아옴
        score += sum(card.execute() for card in scoreSubCard)
        # 여물통 양모 담요 카드등의 경우 execute시 점수 리턴 (가능하면??)
        # 거대 농장은 점수를 얻는 카드나 점수계산이 아닌 낸 즉시 발동하므로 self.score+=n 해주면 될듯??

        self.log_text = f"{self.playerNum}번 플레이어의 점수는 {score} 점입니다"
        return score

    def log(self):
        return self.log_text
