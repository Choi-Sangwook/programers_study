def solution(a, b, n):
    answer = 0
    while n >= a:
        i = n // a
        n = n % a
        answer+=i*b
        n+=i*b
    return answer