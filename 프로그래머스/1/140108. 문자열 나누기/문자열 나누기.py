def solution(s):
    answer = 0
    x = ''
    same = 0
    different = 0
    for char in s:
        if same == 0 and different == 0:
            x = char
        if char == x:
            same += 1
        else:
            different += 1
        if same == different:
            answer += 1
            same = 0
            different = 0
    if same != 0 or different != 0:
        answer += 1
    return answer