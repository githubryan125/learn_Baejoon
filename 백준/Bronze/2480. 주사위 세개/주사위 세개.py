# 같은 눈 3 개 10000 + 같은눈*1000
# 같은 눈 2개 1000 + 같은눈*100
# 모두 다른 눈이 나오면 가장 큰 눈 *100
dice = list(map(int,input().split()))

num=[0]*10
for i in dice:
    num[i]+=1
if max(num)==3:
    print(10000 + dice[0]*1000)
elif max(num)==2:
    print(1000+num.index(max(num))*100)
else:
    print(max(dice)*100)
