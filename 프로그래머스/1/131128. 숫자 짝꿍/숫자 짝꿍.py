def solution(X, Y):
    answer = []

    for i in range(9, -1, -1):
        cnt = min(X.count(str(i)), Y.count(str(i)))
        answer.append(str(i) * cnt)

    result = ''.join(answer)

    if result == '':
        return '-1'

    if result[0] == '0':
        return '0'

    return result