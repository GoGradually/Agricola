"""
현재 행동에 사용 가능한 직업/설비카드가 있는지 검사하는 커맨드 클래스
"""
from command import Command


class CanUseValidation(Command):
    def __init__(self, command):
        self.command = command
    def execute(self):
        #if isfilled[self.command] and self.command.canUse():


        for card in ownCard:
            if card.canUse():
                list.append(card)
        return list

    def log(self):
        pass