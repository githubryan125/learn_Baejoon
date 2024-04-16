# 방 번호
# 플라스틱 1세트 0~9 단, 6은 9랑 교환 가능
# 방 번호가 주어질때 필요한 세트의 최솟값은?
# 그러면 1세트 안에서 해결할 수 없을때 개수를 늘려감
word = input()
ans = [0] * 10
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1
print(max(ans))