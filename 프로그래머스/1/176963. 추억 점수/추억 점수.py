def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]]=yearning[i]
    for i in photo:
        sum = 0
        test = ""
        for k in i:
            if k in score:
                sum+=score[k]
        answer.append(sum)
        print(test)
    return answer