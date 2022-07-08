from curses.ascii import isdigit


def solution(dartResult):
    import re
    regex = r'\d{1,}'
    space = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    digit = list(map(int, re.findall(regex, dartResult)))
    option = re.split(regex, dartResult)[1:]

    for idx, m in enumerate(option):
        for s in m:
            if s in space.keys():
                digit[idx] = pow(digit[idx], space[s])
            else:
                if s == '#': times = -1
                if s == '*': times = 2

                if idx < 1:
                    digit[idx] *= times
                else:
                    if s == '*':
                        digit[idx-1:idx+1] = list(map(lambda x: x * times, digit[idx-1:idx+1]))
                    else:
                        digit[idx] *= times
    return sum(digit)

dartResult = "1D#2S*3S"
print(solution(dartResult))