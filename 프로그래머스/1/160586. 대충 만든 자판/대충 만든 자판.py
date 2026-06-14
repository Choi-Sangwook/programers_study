def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        possible = True
        for char in target:
            min_count = 999
            for key in keymap:
                if char in key:
                    press_count = key.index(char) + 1
                    if press_count < min_count:
                        min_count = press_count
            if min_count == 999:
                possible = False
                break
            cnt += min_count
        if possible:
            answer.append(cnt)
        else:
            answer.append(-1)
    return answer