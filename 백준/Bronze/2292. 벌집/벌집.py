
def find_honeycomb_ring(n):
    if n == 1:
        return 1

    start = 2  # 원의 시작 번호
    end = 7  # 원의 끝 번호
    ring = 2  # 현재 원의 번호

    while True:
        if start <= n <= end:
            return ring
        start = end + 1  # 다음 원의 시작 번호
        end = end + 6 * ring  # 다음 원의 끝 번호
        ring += 1  # 다음 원의 번호 증가


n = int(input())
result = find_honeycomb_ring(n)
print(result)

