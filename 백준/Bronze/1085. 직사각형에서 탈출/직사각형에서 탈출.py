# 현재 한수의 위치 x y
# 왼쪽 아래 0 0
# 오른쪽 꼭짓점은 w h
# 직사각형 경계선까지 가는 거리의 최솟값은 ?

box = list(map(int,input().split()))

min_box  = min(box[2]-box[0],box[3]-box[1],box[0],box[1])
print(min_box)