# n 이 1 일때 넓이는 0
# n , m 을 받아서 최대값과 최솟값을 구해서 넓이 구하기

n=int(input())
if n == 1:
    print(0)
    exit()
min_a,min_b,max_a,max_b=10000,10000,-10000,-10000
for i in range(n):
    a,b=map(int,input().split())
    if a <= min_a:
        min_a=a
    if a >= max_a:
        max_a=a
    if b <= min_b:
        min_b = b
    if b >= max_b:
        max_b = b
print((max_a-min_a)*(max_b-min_b))
