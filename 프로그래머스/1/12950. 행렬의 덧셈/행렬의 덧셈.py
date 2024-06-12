def solution(arr1, arr2):
    # answer 리스트를 동적으로 초기화
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer