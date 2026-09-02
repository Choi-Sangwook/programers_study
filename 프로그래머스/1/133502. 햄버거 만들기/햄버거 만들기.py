def solution(ingredient):
    answer = 0
    stack = []
    for food in ingredient:
        stack.append(food)
        if stack[-4:] == [1,2,3,1]:
            del stack[-4:]
            answer +=1
    return answer
