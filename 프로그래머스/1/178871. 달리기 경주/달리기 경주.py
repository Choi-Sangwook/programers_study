def solution(players, callings):
    # 선수 이름: 현재 위치
    positions = {
        player: index
        for index, player in enumerate(players)
    }

    for called_player in callings:
        # 추월한 선수의 현재 위치
        current_index = positions[called_player]

        # 바로 앞에 있던 선수
        front_player = players[current_index - 1]

        # players 배열에서 두 선수의 위치를 교환
        players[current_index - 1], players[current_index] = (
            players[current_index],
            players[current_index - 1]
        )

        # 딕셔너리에 저장된 위치도 변경
        positions[called_player] = current_index - 1
        positions[front_player] = current_index

    return players