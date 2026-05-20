def solution(wallet, bill):
    answer = 0
    while(min(bill)>min(wallet) or max(bill)>max(wallet)):
        max_index = bill.index(max(bill))
        bill[max_index] //=2
        answer+=1
    return answer