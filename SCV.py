class SCV:
  # 생성자
  def __init__(self, player):
    self.player = player
    self.hp = 60

  def __str__(self):
    return f"[{self.player.name}] SCV ({self.hp}/60)"

  # 멤버 함수: 미네랄 채취
  def harvest(self):
    self.player.mineral += 8

  def attack(self, target):
    target.hp -= 8

