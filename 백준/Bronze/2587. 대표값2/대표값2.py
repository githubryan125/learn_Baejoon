
num=[]
for i in range(5):
    num.append(int(input()))
num.sort()
avg=sum(num)//len(num)
middle=num[len(num)//2]
print(avg)
print(middle)