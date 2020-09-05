# https://app.codesignal.com/interview-practice/task/XP2Wn9pwZW6hvqH67


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverseNodesInKGroups(l, k):
    temp = l
    n = 0

    while temp:
        n += 1
        temp = temp.next
    n = n - (n % k)

    runner = l
    tail = ans = None
    while n > 0:
        cnt = 0

        new_tail = runner 
        new_head = None
        while cnt < k:
            nxt = runner.next
            runner.next = new_head
            new_head = runner
            runner = nxt
            cnt += 1
            n -= 1

        if not ans:
            ans = new_head

        if tail:
            tail.next = new_head

        tail = new_tail

    tail.next = runner

    return ans

# recursive version
def recursive(l, k):

    tmp = l
    for _ in range(k):
        if not tmp:
            return l
        tmp = tmp.next

    run = l
    prev_tail = None
    for _ in range(k):
        next_node = run.next
        run.next = prev_tail
        prev_tail = run
        run = next_node

    l.next = recursive(run, k)

    return prev_tail


cases = [
        [[1, 2, 3, 4, 5], 2],       # [2, 1, 4, 3, 5]
        [[1, 2, 3, 4, 5], 1],       # [1, 2, 3, 4, 5]
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3],   # [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11]
        ]
for list1, k in cases:
    l = temp = ListNode(list1[0])
    for li in list1[1: ]:
        temp.next = ListNode(li)
        temp = temp.next

    #ans = reverseNodesInKGroups(l, k)
    ans = recursive(l, k)
    while ans:
        print(ans.value, end = ' ')
        ans = ans.next
    print()
