
def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) - 1):
        if phone_book[idx + 1].startswith(phone_book[idx]):
            return False
        else:
            continue
    return True

case = [
        ["119", "97674223", "1195524421"],  # false
        ["123","456","789"],                # true
        ["12","123","1235","567","88"]      # false
        ]
for c in case:
    print(solution(c))
