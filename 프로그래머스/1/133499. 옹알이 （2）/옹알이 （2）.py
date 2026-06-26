def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        i = 0
        prev = ""
        can_say = True
        while i < len(word):
            matched = False
            for sound in possible:
                if word[i:i+len(sound)] == sound:
                    if sound == prev:
                        can_say = False
                        break

                    prev = sound
                    i += len(sound)
                    matched = True
                    break
            if not matched:
                can_say = False
                break
            if not can_say:
                break
        if can_say:
            answer += 1
    return answer