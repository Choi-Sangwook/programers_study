def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    n = 0
    r = len(score)//m
    for i in range(1,r+1):
        n=i*m-1
        answer+=(score[n]*m)
    return answer