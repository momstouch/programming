# https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    temp1 = l
    temp2 = None

    while temp1:
        if temp1.value == k:
            if temp2:
                temp2.next = temp1.next
            else:
                l = temp1.next
        else:
            temp2 = temp1

        temp1 = temp1.next

    return l


cases = [
        [[3, 1, 2, 3, 4, 5], 3],
        [[1000, 1000], 1000],
        ]
for numbers, k in cases:
    l = temp = ListNode(numbers[0])
    for n in numbers[1:]:
        temp.next = ListNode(n)
        temp = temp.next

    answer = removeKFromList(l, k)
    while answer:
        print(answer.value, end = ' ')
        answer = answer.next
    print()
