def solution(sizes):
    answer = 0
    max_ans=0
    min_ans=0
    ans=0
    for i in range(len(sizes)):
        now=max(sizes[i][0],sizes[i][1])
        if now >= ans:
            ans = now
            max_ans,min_ans = max(sizes[i][0],sizes[i][1]),min(sizes[i][0],sizes[i][1])
    for j in range(len(sizes)):
        if sizes[j][0] > min_ans and sizes[j][1] > min_ans:
            min_ans=min(sizes[j][0],sizes[j][1])
    answer=max_ans * min_ans
    return answer