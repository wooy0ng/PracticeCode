def solution(s):
  return '*' * (len(s) - 4) + s[-4:]

phone_number = "01033334444"	
print(solution(phone_number))