score= input()
num=[]
ans=""
for i in range(len(score)):
    num.append(int(score[i]))
num.sort(reverse=True)
for k in num:
    ans+=f"{k}"
print(ans)