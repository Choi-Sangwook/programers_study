def solution(cards1, cards2, goal):
    answer = []
    check1 = 0
    check2 = 0
    for word in goal:
        
        if check1 < len(cards1) and cards1[check1] == word:
            check1 += 1

        elif check2 < len(cards2) and cards2[check2] == word:
            check2 += 1
        else:
            return 'No'
    return 'Yes'