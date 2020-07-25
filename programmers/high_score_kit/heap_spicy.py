# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


# brute force
def solution(scoville, K):
    cnt = 0

    scoville.sort()

    while len(scoville) >= 2 and scoville[0] < K:
        s = scoville.pop(1)
        scoville[0] += s * 2

        scoville.sort()
        cnt += 1

    if scoville and scoville[0] > K:
        return cnt
    else:
        return -1


def solution2(scoville, K):
    cnt = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + m2 * 2)
        cnt += 1

    if scoville and scoville[0] > K:
        return cnt
    else:
        return -1


cases = [
        [[1, 2, 3, 9, 10, 12], 7],      # 2
        ]
for sc, k in cases:
    print(solution2(sc, k))
    #print(solution(sc, k))
