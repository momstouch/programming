# https://app.codesignal.com/interview-practice/task/5vcioHMkhGqkaQQYt

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def rearrangeLastN(l, n):
    if not n:
        return l

    tail = l
    cnt = size = 0
    while tail:
        if not tail.next:
            size += 1
            break

        tail = tail.next
        size += 1

    if size == n:
        return l

    new_tail = l
    while cnt + n < size - 1:
        new_tail = new_tail.next
        cnt += 1

    if new_tail.next:
        new_head = new_tail.next
        new_tail.next = None
    else:
        new_head = l

    tail.next = l

    return new_head


def better_code(l, n):
    if not n:
        return l

    new_tail, mid = l, l
    for _ in range(n):
        mid = mid.next

    if not mid:
        return l

    while mid.next:
        mid = mid.next
        new_tail = new_tail.next

    ans = new_tail.next
    new_tail.next = None
    mid.next = l

    return ans


cases = [
        [[1, 2, 3, 4, 5], 3],       # [3, 4, 5, 1, 2]
        [[1, 2, 3, 4, 5, 6, 7], 1], # [7, 1, 2, 3, 4, 5, 6]
        [[1000, -1000], 0],         # [1000, -1000]
        [[123, 456, 789, 0], 4],    # [123, 456, 789, 0]
        ]
for li, n in cases:
    l = temp = ListNode(li[0])
    for ele in li[1:]:
        temp.next = ListNode(ele)
        temp = temp.next

    #ans = rearrangeLastN(l, n)
    ans = better_code(l, n)
    while ans:
        print(ans.value, end = ' ')
        ans = ans.next
    print()
