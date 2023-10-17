def solution(players, callings):
    positions = {}
    for i in range(len(players)):
        positions[players[i]] = i
    for j in callings:
        faster_index = positions[j]
        changed_index = faster_index - 1
        if changed_index >= 0:  # 범위를 벗어나지 않도록 확인
            players[faster_index], players[changed_index] = players[changed_index], players[faster_index]
            # positions 딕셔너리를 업데이트
            positions[players[faster_index]] = faster_index
            positions[players[changed_index]] = changed_index
    
    answer = players
    return answer
