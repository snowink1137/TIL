def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))

    for i in range(len(phone_book)):
        length = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:length]:
                return False

    return answer


# phone_book = ['119', '97674223', '1195524421']
phone_book = ['12', '123', '1235', '567', '88']
print(solution(phone_book))

