def solution(phone_book):
    phone_book.sort()
    dict_ = {idx: phone_book[idx] for idx in range(len(phone_book))}
    
    for idx in range(len(phone_book)-1):
        if dict_[idx] in dict_[idx+1][:len(dict_[idx])]:
            return False
    return True


# phone_book =  ["97674223","119", "1195524421"]	
phone_book =  ["97674223", "976"]	
print(solution(phone_book))