# 초기 플레이어 설정
# 플레이어와 시작 건물 / 유닛을 생성한다.
from CommandCenter import CommandCenter
from Player import Player
from SCV import SCV

player = Player('BoxeR')
commandCenter = CommandCenter(player)
scvList = [
    SCV(player),
    SCV(player),
    SCV(player),
    SCV(player),
]

# 건설로봇 생산
newScv = commandCenter.produce()
scvList.append(newScv)

# 미네랄 채취
for scv in scvList:
    scv.harvest()

# 플레이어 정보 출력
print(player)

scvList[0].attack(scvList[1])
print(scvList[1])
