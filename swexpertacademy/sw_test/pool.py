# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def solution(costs, plan):
    i = 0
    m1s = [0]
    while i < len(plan):
        print(i, m1s)
        m1 = min(plan[i] * costs[0], costs[1]) + m1s[-1]
        m1s.append(m1)
        i += 1

        if len(m1s) > 3:
            print(i, m1s, m1s[i-3] + costs[2])
            m1s[-1] = min(m1s[-1], m1s[i - 3] + costs[2])

    return min(costs[-1], m1s[-1])

if __name__ == "__main__":
    t = int(input()) # test case
    for i in range(t):
        costs = list(map(int, input().rstrip().split(' ')))
        plan = list(map(int, input().rstrip().split(' ')))
        if True:#i == 6:
            print("#%d" % (i+1), solution(costs, plan))
