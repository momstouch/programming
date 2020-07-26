# https://programmers.co.kr/learn/courses/30/lessons/42629
class Node:
    def __init__(self, take, date, val, skip):
        self.take = take
        self.date = date
        self.val = val
        self.skip = skip


def solution(stock, dates, supplies, k):
    head = Node(None, stock, None)
    temp = head
    now = 0
    for date, supply in zip(dates, supplies):
        take_val = stock - (date - now) + supply
        take = Node(None, date, take_val, None)
        skip_val = stock - (date - now)
        skip = Node(None, date, skip_val, None)
        temp.take = take
        temp.skip = skip
        now = date



cases = [
        [4, [4, 10, 15], [20, 5, 10], 30],  # 2
        ]
for case in cases:
    print(solution(case[0], case[1], case[2], case[3]))
