# 삼각형 외우기
# 3 각의 크기 가 모두 60 이면 Equilateral
# 3각의 합이 180 이고 두각이 같을때
# 3각의 합이 180 이고 같은 각이 없을때
# else error

# 1.  세각의 합이 180 일때
# 1-1 .각 각의 크기가 3,2,1개가 같을때 경우 3가지
# 2. else -> error

a=int(input())
b=int(input())
c=int(input())

if a+b+c==180:
    if a == b == c == 60:
        print("Equilateral")
    elif a==b or b==c or a ==c :
        print("Isosceles")
    elif a!=b and b!=c and a!=c:
        print("Scalene")
else:
    print("Error")
