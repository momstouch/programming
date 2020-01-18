# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Runtime: 80 ms
    # Memory Usage: 12.8 MB
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(0)

        flag = 0
        while l1 and l2:
            val = l1.val + l2.val + flag
            if val > 9:
                flag = 1
                val = val % 10
            else:
                flag = 0

            temp.next = ListNode(val)

            l1 = l1.next
            l2 = l2.next
            temp = temp.next

        remain = l1 if l1 else l2
        while remain:
            val = remain.val + flag
            if val > 9:
                val = val % 10
                flag = 1
            else:
                flag = 0

            temp.next = ListNode(val)
            temp = temp.next
            remain = remain.next

        if flag:
            temp.next = ListNode(1)

        return head.next


    # Runtime: 56 ms
    # Memory Usage: 12.7 MB
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(0)

        flag = 0
        while l1 and l2:
            val = l1.val + l2.val + flag
            flag = val // 10
            if flag:
                val = val % 10

            l1.val = val
            temp.next = l1

            l1 = l1.next
            l2 = l2.next
            temp = temp.next

        remain = l1 if l1 else l2
        while remain:
            val = remain.val + flag
            flag = val // 10
            if flag:
                val = val % 10

            remain.val = val
            temp.next = remain

            remain = remain.next
            temp = temp.next

        if flag:
            temp.next = ListNode(1)

        return head.next


A = [2, 4, 3]
B = [5, 6, 4]

A = [1, 8]
B = [0]

A = [1]
B = [9, 9]

a_head = a_temp = ListNode(A[0])
for a in A[1:]:
    a_temp.next = ListNode(a)
    a_temp = a_temp.next
b_head = b_temp = ListNode(B[0])
for b in B[1:]:
    b_temp.next = ListNode(b)
    b_temp = b_temp.next

result = Solution().addTwoNumbers_2(
        a_head, b_head
        )

while result:
    print(result.val, end=' ')
    result = result.next

print()
