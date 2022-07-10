

def solution(new_id):
    answer = ''

    # round 1
    new_id = new_id.lower()
    
    # round 2
    import re
    regex = r'[a-z0-9-_.]'
    pattern = re.compile(regex)
    new_id = ''.join(pattern.findall(new_id))

    # round 3
    regex = r'[.]{2,}'
    pattern = re.compile(regex)
    new_id = re.sub(pattern, '.', new_id)

    # round 4
    if len(new_id) > 0:
        if new_id[0] == '.' :
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # round 5
    if len(new_id) == 0:
        new_id += 'a'
    
    # round 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # round 7
    if len(new_id) <= 2:
        while True:
            new_id += new_id[-1]
            if len(new_id) == 3:
                break
    answer = new_id
    return answer

new_id = "=.="
solution(new_id)