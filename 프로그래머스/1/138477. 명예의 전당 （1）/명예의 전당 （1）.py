def solution(k, score):
    answer = []
    ls = []
    for i in range(len(score)):
        ls.append(score[i])
        ls.sort(reverse=True)
        if(len(ls)<k):
            answer.append(ls[(len(ls)%k)-1])
        else:
            answer.append(ls[k-1])
    return answer