def solution(s):
    string = ""
    base = 1
    answer = []
    while base < len(s):
        list_ = [s[idx:idx+base] for idx in range(0, len(s), base)]
        n = 0
        chr = list_[n]
        for idx in range(len(list_)-1):
            if list_[idx] == list_[idx+1]:
                n += 1
            else:
                if n:
                    string += f"{n+1}{chr}"
                else:
                    string += chr
                chr = list_[idx+1]
                n = 0
        if n:
            string += f"{n+1}{chr}"
        else:
            string += chr
        base += 1
        answer.append(len(string))
        string = ""
    return min(answer) if answer else 1

s = "ababcdcdababcdcd"	
print(solution(s))