import re

def solution(new_id):
    st = new_id
    st = st.lower()
    # round 1
    st = re.sub('[^a-z0-9\-_.]', '', st)

    # round 2
    st = re.sub('[.]{2,}', '.', st)

    # round 3
    '''
    ^ : 문장의 처음
    $ : 문장의 끝
    '''
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st