# a b c d e f 가 주어진다.
# 이때의 x y 값을 구하라
vr= list(map(int,input().split()))

for i in range(-999,1000):
    for j in range(-999, 1000):
        if vr[0]*i + vr[1]*j ==vr[2] and vr[3]*i + vr[4]*j ==vr[5]:
            print(i, j,end=" ")