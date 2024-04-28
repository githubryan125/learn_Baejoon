# 막대기로 만들 수 있는 삼각형의 최대 둘레 ?

tri = list(map(int, input().split()))
tri.sort()
print(tri[0]+tri[1]+min(tri[2],tri[0]+tri[1]-1))



# 제일 큰수 제외한 사각형의 대각선 길이
