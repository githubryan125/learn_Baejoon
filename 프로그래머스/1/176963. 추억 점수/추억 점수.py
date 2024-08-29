def solution(name, yearning, photo):
    
    result = []
    for people in photo:
        score = 0
        for person in people:
            # person이 name 배열에 있는지 확인
            if person in name:
                # person의 인덱스를 통해 yearning 배열에서 점수 가져오기
                index = name.index(person)
                score += yearning[index]
        result.append(score)
    
    return result
