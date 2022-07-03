import re

'''
# regex 문법
^ : 문자열의 시작
$ : 문자열의 끝
'''

def solution(phoneBook):
    for b in phoneBook:
        p = re.compile("^"+b)
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True
