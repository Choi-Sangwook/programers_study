def solution(s, skip, index):
    answer = ''
    skip = set(skip)

    for ch in s:
        count = 0
        code = ord(ch)

        while count < index:
            code += 1

            if code > ord('z'):
                code = ord('a')

            if chr(code) in skip:
                continue

            count += 1

        answer += chr(code)

    return answer