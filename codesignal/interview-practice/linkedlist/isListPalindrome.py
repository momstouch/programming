# https://app.codesignal.com/interview-practice/task/HmNvEkfFShPhREMn4

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def isListPalindrome(l):
    # find the mid node
    # tail is twice as fast as mid
    mid = tail = head = l
    while tail and tail.next:
        tail = tail.next.next
        mid = mid.next

    rev_head = None
    while mid:
        next_node = mid.next
        mid.next = rev_head
        rev_head = mid
        mid = next_node

    while rev_head:
        if rev_head.value != head.value:
            return False
        rev_head = rev_head.next
        head = head.next

    return True


cases = [
        [0, 1, 0],              # true
        [1, 2, 2, 3],           # false
        [1, 2, 3, 1, 2, 3],     # false
        ]

for case in cases:
    l = temp = ListNode(case[0])
    for elmt in case[1:]:
        temp.next = ListNode(elmt)
        temp = temp.next

    print(isListPalindrome(l))
