def solution(phone_number):
    num_len = len(phone_number)
    answer = ''
    answer = "*"*(num_len-4)
    answer = answer+phone_number[num_len-4:]
    return answer