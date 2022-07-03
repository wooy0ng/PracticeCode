def solution(participant, completion):
    dict_ = {}
    participant.sort()
    completion.sort()

    for name in participant:
        if name not in dict_:
            dict_[name] = 1
        else:
            dict_[name] += 1

    for name in completion:
        dict_[name] -= 1
        if not dict_[name]:
            del dict_[name]

    answer = [name for name in dict_.keys() if dict_[name]]
    return answer[0] if answer else ""



participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]	

print(solution(participant, completion))