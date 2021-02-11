# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def minimumBribes(q):
    ans = 0
    # q would have the same values as indices
    q = [p-1 for p in q]

    for i, p in enumerate(q):
        # an element can bribe the others only twice
        if p - i > 2:
            print("Too chaotic")
            return "Too chaotic"

        # an element who bribes p can be in front of p's original position
        # so we can count elements who bribe p only from p-1 to
        # in front of p's current position 
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                ans += 1
    print(ans)
    return ans


cases = [
        ([2,1,5,3,4], 3),
        ([2,5,1,3,4], "Too chaotic"),
        ([5,1,2,3,7,8,6,4], "Too chaotic"),
        ([1,2,5,3,7,8,6,4], 7),
        ([1,2,5,3,4,7,8,6], 4),
        ]
for q, answer in cases:
    assert minimumBribes(q) == answer
