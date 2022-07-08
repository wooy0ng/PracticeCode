def solution(phone_number):
    answer = ""
    for _ in phone_number[:-4]:
        answer += "*"
    return answer + phone_number[-4:]

phone_number = "01033334444"	
print(solution(phone_number))