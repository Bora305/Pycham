class Player:
  # 생성자
  def __init__(self, name):
    self.name = name
    self.mineral = 50

  # 멤버 함수: 생성자와 같이 예약된 멤버 함수이며, 인스턴스를 문자열로 표현할 때 원하는 형태로 표현할 수 있다.
  # 전에 실습했던 printInfo 와 유사한 역할을 한다. (차이점은 print 하지 않고 문자로 반환한다는 점)
  def __str__(self):
    return f"{self.name}님의 보유 미네랄 양은 {self.mineral} 입니다."