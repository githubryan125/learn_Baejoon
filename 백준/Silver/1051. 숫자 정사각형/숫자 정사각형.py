n, m = map(int, input().split())
box = [list(input()) for _ in range(n)]
end = min(n, m)  # 변수로 사용
large = 1
for i in range(1, end + 1):
    for j in range(n):
        for k in range(m):
            if 0 < j + i < n and 0 < k + i < m:  # m을 수정
                if box[j][k] == box[j + i][k + i] == box[j + i][k] == box[j][k + i]:
                    large = (i + 1) * (i + 1)
print(large)
