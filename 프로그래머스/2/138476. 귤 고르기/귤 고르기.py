from collections import Counter

def solution(k, tangerine):
    answer = 0
    now = 0

    # Count the frequency of each tangerine size
    size_count = Counter(tangerine)
    
    # Sort sizes by their frequency in descending order
    sorted_counts = sorted(size_count.values(), reverse=True)
    
    # Accumulate counts until we reach at least `k`
    for count in sorted_counts:
        now += count
        answer += 1
        if now >= k:
            break
    
    return answer
