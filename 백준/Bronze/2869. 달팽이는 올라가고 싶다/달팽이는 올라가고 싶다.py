# 달팽이는 올라가고 싶다
# v 미터 막대를 오른다
# 낮 A 미터 오름 밤 에는 B 미끄러짐
# 정상에 오르면 미끄러지지 않는다 .
# 정상에 오르려면 며칠이 걸리는가 ?

# #  A B V 가 주어진다.
import math
snail = list(map(int,input().split()))

day = (snail[2]-snail[1]) / (snail[0]-snail[1])
print(math.ceil(day))