import sys

n = int(sys.stdin.readline())
coordinates = list(map(int, sys.stdin.readline().split()))

# 중복 제거 및 정렬
sorted_coords = sorted(set(coordinates))

# 좌표를 압축하기 위한 딕셔너리 생성
compress_dict = {coord: index for index, coord in enumerate(sorted_coords)}

# 결과 출력
for coord in coordinates:
    print(compress_dict[coord], end=" ")
