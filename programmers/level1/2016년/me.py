from calendar import week


def solution(a, b):
    import datetime
    weekdays = {
        0: 'MON',
        1: 'TUE',
        2: 'WED',
        3: 'THU',
        4: 'FRI',
        5: 'SAT',
        6: 'SUN'
    }
    weekday = datetime.date(2016, a, b).weekday()
    return weekdays[weekday]

a = 5 
b = 24
print(solution(a, b))