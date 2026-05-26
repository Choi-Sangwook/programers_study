def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
def solution(signals):
    cycles = []
    for G,Y,R in signals:
        cycles.append(G+Y+R)
    limit = cycles[0]
    for i in range(1, len(cycles)):
        limit = lcm(limit, cycles[i])
    for t in range(1,limit+1):
        all_yellow = True
        for G,Y,R in signals:
            cycle = G+Y+R
            pos = (t-1)%cycle
            if not (G <= pos < G+Y):
                all_yellow = False
                break
        if all_yellow:
            return t
    return -1