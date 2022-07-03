def solution(answers):
    def mk_list(x):
        return x * (len(answers) // len(x)) + x[:len(answers)%len(x)]
    cnt = [0] * 3
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a = mk_list(a)
    b = mk_list(b)
    c = mk_list(c)

    for idx, (k, l, m) in enumerate(zip(a, b, c)):
        if answers[idx] == k: cnt[0] += 1
        if answers[idx] == l: cnt[1] += 1
        if answers[idx] == m: cnt[2] += 1
    
    answer = list(filter(lambda idx: cnt[idx] == max(cnt), range(len(cnt))))
    return [n+1 for n in answer]