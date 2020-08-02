# https://programmers.co.kr/learn/courses/30/lessons/42629
import heapq


# time over
def solution_brute(stock, dates, supplies, k):
    pq = []
    ans = 0
    for day in range(k):
        if dates and dates[0] == day:
            dates.pop(0)
            heapq.heappush(pq, -supplies.pop(0))

        if stock == 0:
            stock = -heapq.heappop(pq)
            ans += 1

        stock -= 1

    return ans


def solution(stock, dates, supplies, k):
    pq = []
    ans = 0
    idx = 0
    # once I use pop() for dates and supplies,
    # that code couldn't pass on effectiveness test

    while stock < k:
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                heapq.heappush(pq, -supplies[i])
                idx += 1
            else:
                break

        if not pq:
            return ans

        stock -= heapq.heappop(pq)
        ans += 1

    return ans


cases = [
        [4, [4, 10, 15], [20, 5, 10], 30],  # 2
        ]
for case in cases:
    print(solution(case[0], case[1], case[2], case[3]))
