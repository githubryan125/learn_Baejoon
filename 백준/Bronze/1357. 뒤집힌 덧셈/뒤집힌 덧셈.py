x,y=input().split()

x=int(x[::-1])
y=int(y[::-1])

result=str(x+y)
result=int(result[::-1])

print(result)