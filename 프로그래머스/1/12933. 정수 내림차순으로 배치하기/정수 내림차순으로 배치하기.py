def solution(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n //= 10
    arr.sort(reverse=True)
    return int("".join(map(str, arr)))