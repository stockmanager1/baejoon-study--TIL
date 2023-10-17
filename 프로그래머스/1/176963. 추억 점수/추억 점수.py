def solution(name, yearning, photo):
    friends = dict(zip(name, yearning))
    
    result = []
    for i in range(len(photo)):
        out = sum(friends.get(j, 0) for j in photo[i])  # friends.get(j, 0)은 이름 j에 대한 yearning 값을 반환하거나, j가 없으면 0을 반환합니다.
        result.append(out)
    
    return result
