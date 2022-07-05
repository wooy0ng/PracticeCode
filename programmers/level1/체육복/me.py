def solution(n, lost, reserve):
    list_ = [0 if k in lost else 1 for k in range(1, n+1)]
    for idx in range(len(list_)):
        if idx + 1 in reserve:
            list_[idx] += 1

    for idx, k in enumerate(list_):
        if idx == 0:
            prev = 0
        else:
            prev = idx - 1
        
        if idx == len(list_) - 1:
            next = idx
        else:
            next = idx + 1
        
        if not k:
            if list_[prev] == 2:
                list_[prev] -= 1                
                list_[idx] += 1
            elif list_[next] == 2:
                list_[next] -= 1
                list_[idx] += 1
    return sum([1 if k else 0 for k in list_])


n = 2
lost = [1]
reserve = [2]
print(solution(n, lost, reserve)) # 4