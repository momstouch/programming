# https://app.codesignal.com/interview-practice/task/RvDFbsNC3Xn7pnQfH

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def addTwoHugeNumbers(a, b):
    temp = a
    a_rev = None
    while temp:
        next_node = temp.next
        temp.next = a_rev
        a_rev = temp
        temp = next_node

    temp = b
    b_rev = None
    while temp:
        next_node = temp.next
        temp.next = b_rev
        b_rev = temp
        temp = next_node

    answer = None
    flag = 0
    while a_rev or b_rev or flag:
        aval = a_rev.value if a_rev else 0
        bval = b_rev.value if b_rev else 0

        ans = aval + bval + flag
        flag = 1 if ans > 9999 else 0
        ans = ans % 10000
        
        temp = ListNode(ans)
        temp.next = answer
        answer = temp

        a_rev = a_rev.next if a_rev else None
        b_rev = b_rev.next if b_rev else None

    return answer


cases = [
        [[9876, 5432, 1999], [1, 8001]],    # [9876, 5434, 0]
        [[123, 4, 5], [100, 100, 100]],     # [223, 104, 105]
        [[0], [1234, 123, 0]],              # [1234, 123, 0]
        ]
for aaa, bbb in cases:
    a = temp = ListNode(aaa[0])
    for aa in aaa[1:]:
        temp.next = ListNode(aa)
        temp = temp.next

    b = temp = ListNode(bbb[0])
    for bb in bbb[1:]:
        temp.next = ListNode(bb)
        temp = temp.next

    answer = addTwoHugeNumbers(a, b)
    while answer:
        print(answer.value, end = ' ')
        answer = answer.next
    print()
