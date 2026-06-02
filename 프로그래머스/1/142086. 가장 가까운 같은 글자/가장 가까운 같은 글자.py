def solution(s):
    answer = []
    for i in range(len(s)):
        if i == 0:
            answer.append(-1)
            continue
        for k in range(i-1,-1,-1):
            if s[i] == s[k]:
                answer.append(i-k)
                break
            if k == 0:
                answer.append(-1)
    return answer