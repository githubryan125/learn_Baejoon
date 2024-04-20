import sys

n =int(sys.stdin.readline())
for i in range(1,n+1):
    a,b=map(int,sys.stdin.readline().split())
    case=a+b
    print(f"Case #{i}: {a} + {b} = {case}")