# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    sorted_book = sorted(phone_book)
    n = len(phone_book)

    for i in range(n - 1):
        size = len(sorted_book[i])
        for j in range(i + 1, n):
            if sorted_book[i] == sorted_book[j][0:size]:
                return False

    return True


def solution2(phone_book):
    sorted_book = sorted(phone_book)

    for x, y in zip(sorted_book, sorted_book[1:]):
        if y.startswith(x):
            return False

    return True


phone_book = ["119", "97674223", "1195524421"]
# return false

print(solution(phone_book))
print(solution2(phone_book))
