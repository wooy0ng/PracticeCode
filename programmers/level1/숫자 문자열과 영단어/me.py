def solution(s):
    answer = ""
    dictionary = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8', 
        'nine': '9'
    }
    tmp = ""

    # dictionary 객체의 메소드를 얼마나 잘 활용하느냐에 대한 문제임
    # pythonic하지 않은 내 코드
    # dict.replace(key, value)
    for c in list(s):
        if c in "0123456789":
            answer += c
        else:
            tmp += c
            if tmp in dictionary.keys():
                answer += dictionary[tmp]
                tmp = ""
    return int(answer)


s = "one4seveneight"
solution(s)