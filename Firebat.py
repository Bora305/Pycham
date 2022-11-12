class Firebat:
  # 생성자
  def __init__(self, player):
    self.player = player
    self.hp = 50

  def __str__(self):
    return f"[{self.player.name}] Firebat ({self.hp}/50)"

  def attack(self):
    target.hp -= 16
