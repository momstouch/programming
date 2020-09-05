# https://app.codesignal.com/interview-practice/task/6rE3maCQwrZS3Mm2H


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(l1, l2):
    # recursive
    # need sys.setrecursionlimit(10**5)

    if not l1:
        return l2
    if not l2:
        return l1

    if l1.value < l2.value:
        temp = l1
        temp.next = mergeTwoLinkedLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeTwoLinkedLists(l1, l2.next)

    return temp


def non_recursive(l1, l2):
    head = temp = ListNode(None)

    while l1 and l2:
        if l1.value < l2.value:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next

    temp.next = l1 if l1 else l2 if l2 else None
    return head.next


cases = [
        [[1, 2 ,3], [4, 5, 6]],         # [1, 2, 3, 4, 5, 6]
        [[5, 10, 15, 40], [2, 3, 20]],   # [2, 3, 5, 10, 15, 20, 40]
        ]
for list1, list2 in cases:
    l1 = temp = ListNode(list1[0])
    for li in list1[1: ]:
        temp.next = ListNode(li)
        temp = temp.next
    l2 = temp = ListNode(list2[0])
    for li in list2[1: ]:
        temp.next = ListNode(li)
        temp = temp.next

    #ans = mergeTwoLinkedLists(l1, l2)
    ans = non_recursive(l1, l2)
    while ans:
        print(ans.value, end = ' ')
        ans = ans.next
    print()
