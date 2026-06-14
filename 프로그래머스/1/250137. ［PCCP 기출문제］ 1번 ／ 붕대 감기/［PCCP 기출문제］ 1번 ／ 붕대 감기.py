def solution(bandage, health, attacks):
    answer = 0
    cur_health = health
    cur_time = 0
    suc_time = 0
    cur_attack = 0
    for attack in range(attacks[-1][0]+1):
        if(cur_time==attacks[cur_attack][0]):   #공격 당했을때
            cur_health -=attacks[cur_attack][1]
            if cur_health <= 0:
                return -1
            cur_attack+=1
            suc_time = 0
            cur_time+=1
        else:                                   #공격 안당했을때
            suc_time += 1
            cur_health += bandage[1]

            if suc_time == bandage[0]:
                cur_health += bandage[2]
                suc_time = 0
            cur_time+=1
            if cur_health >= health:
                cur_health = health
    return cur_health