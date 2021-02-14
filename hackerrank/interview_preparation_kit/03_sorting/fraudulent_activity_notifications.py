# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# TODO

from heapq import heappush, heappop, heapify

class WindowingMedian:
    def __init__(self, sequence, window_size):
        self.seq = sequence
        self.window = window_size
        self.lowers, self.highers = [], []

        for s in self.seq[: self.window]:
            self.add_number(s)
        self.rebalance()

        self.pos = self.window

    def sliding(self):
        if self.pos > len(self.seq):
            return False
        left_most = self.seq[self.pos - self.window]
        self.rm_number(left_most)
        self.add_number(self.seq[self.pos])
        self.pos += 1

        self.rebalance()

        return True

    def add_number(self, number):
        if not self.highers or number > self.highers[0]:
            heappush(self.highers, number)
        else:
            heappush(self.lowers, -number)  # for lowers we need a max heap
        #self.rebalance()

    def rm_number(self, number):
        if self.highers and number in self.highers:
            i = self.highers.index(number)
            del self.highers[i]
            heapify(self.highers)
        elif self.lowers and -number in self.lowers:
            i = self.lowers.index(-number)
            del self.lowers[i]
            heapify(self.lowers)

    def rebalance(self):
        while True:
            if len(self.lowers) - len(self.highers) > 1:
                heappush(self.highers, -heappop(self.lowers))
            elif len(self.highers) - len(self.lowers) > 1:
                heappush(self.lowers, -heappop(self.highers))
            else:
                break

    def get_median(self):
        if len(self.lowers) == len(self.highers):
            return (-self.lowers[0] + self.highers[0])/2
        elif len(self.lowers) > len(self.highers):
            return -self.lowers[0]
        else:
            return self.highers[0]

# time limit violation error
def activityNotifications_timelimit(expenditure, d):
    ans = 0
    if len(expenditure) < d + 1:
        return ans

    # running median problem
    wm = WindowingMedian(expenditure, d)
    for e in expenditure[d:]:
        med = wm.get_median()
        if med * 2 <= e:
            ans += 1

        wm.sliding()

    return ans

from collections import Counter
def activityNotifications(expenditure, d):
    ans = 0

    mid1, mid2 = (d - 1) // 2, (d - 1) // 2 + (1 if d % 2 == 0 else 0)

    # for count sort
    dic = Counter(expenditure[:d])
    cs = [dic[i] if i in dic else 0 for i in range(max(expenditure) + 1)]

    for i, e in enumerate(expenditure[d:], start = d):

        k = 0
        m1, m2 = None, None
        for j, cnt in enumerate(cs):
            k += cnt
            if m1 is None and k > mid1:
                m1 = j
            if m2 is None and k > mid2:
                m2 = j
                break

        med = (m1 + m2) / 2.0
        if med * 2.0 <= e:
            ans += 1

        cs[expenditure[i - d]] -= 1
        cs[expenditure[i]] += 1

    return ans


cases = [
        ([10,20,30,40,50], 3, 1),
        ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2),
        ([1,2,3,4,4], 4, 0),
        ]
for expenditure, d, answer in cases:
    assert activityNotifications(expenditure, d) == answer
