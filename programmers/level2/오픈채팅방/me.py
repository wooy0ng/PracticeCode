
def solution(record):
    '''
    제한 사항에 반복 횟수가 1000개 이상이면
    최대한 중첩 for문은 피해보자.
    '''
    answer, status = [], []
    dictionary = {}
    for string in record:
        split_ = string.split()
        if split_[0] == 'Enter' or split_[0] == 'Change':
            dictionary.update({split_[1]: split_[2]})
        status.append([split_[0], split_[1]])
    
    for s, id in status:
        if s == 'Enter':
            answer.append(f"{dictionary[id]}님이 들어왔습니다.")
        elif s == 'Leave':
            answer.append(f"{dictionary[id]}님이 나갔습니다.")
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))