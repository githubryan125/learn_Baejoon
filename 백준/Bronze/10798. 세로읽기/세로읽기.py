number=[list(input()) for _ in range(5)]
answer=''
for i in range(15):
    for j in range(5):
        if len(number[j]) > i:
            answer+=number[j][i]
print(answer)
