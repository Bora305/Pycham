# 클래스: 사령부
from SCV import SCV


class CommandCenter:
  # 생성자
   def __init__(self, player):
    self.player = player

  # 멤버 함수: 유닛 생성
   def produce(self):
    self.player.mineral -= 50
    f = open("log.csv", 'a')
    f.write(f"{self.player.name},건설로봇,생성,1")
    f.close()
    return SCV(self.player)
