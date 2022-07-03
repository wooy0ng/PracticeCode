

def solution(id_list, report, k):
    answer = []
    dictionary = {}
    for id in id_list:
        dictionary.update({
            id: {"warning": 0, "user_reported": set([])}
        })

    for data in report:
        alice, bob = data.split(" ")
        if bob not in dictionary[alice]['user_reported']:
            dictionary[alice]['user_reported'].add(bob)
            dictionary[bob]['warning'] += 1

    stopped_users = set([user for user in dictionary.keys() if dictionary[user]['warning'] >= k])
    for user in dictionary.keys():
        answer.append(len(dictionary[user]['user_reported'] & stopped_users))
    return answer

k = 2
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
solution(id_list, report, k)
    