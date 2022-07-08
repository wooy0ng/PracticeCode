import enum
import collections

def solution(N, stages):
    '''
    from collections import Counter가 있었음...
    '''
    dict_ = {i: 0 for i in range(1, N+2)}
    for stage in stages:
        dict_[stage] += 1
    
    result = []
    for stage in dict_.keys():
        if stage > N:
            break
        clear_users = 0
        current_users = dict_[stage]
        while stage <= N+1:
            clear_users += dict_[stage]
            stage += 1
        result.append(current_users / clear_users if clear_users > 0 else 0)
    result = sorted([(idx+1, per) for idx, per in enumerate(result)], key=lambda x: x[1], reverse=True)  
    return [idx for idx, _ in result]

N = 5   # 전체 스테이지의 개수
stages = [2]       # 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호
print(solution(N, stages))