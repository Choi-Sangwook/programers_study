def solution(food):
    answer = ''
    menu = []
    for i in range(len(food)):
        if not food[i]//2 == 0:
            for r in range(food[i]//2):
                answer+=str(i)
                menu.append(i)
    answer+='0'
    for i in range(len(menu)-1,-1,-1):
        answer+=str(menu[i])
    return answer