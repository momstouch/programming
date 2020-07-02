# https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    ans = []
    released = []
    completed = []
    n = len(progresses)

    def get_n_sum(n):
        return ((n + 1) * n) // 2

    while len(released) < n:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    completed.append(i + 1)
                    n_sum = get_n_sum(max(completed))

                    if sum(released) + sum(completed) == n_sum:
                        ans.append(len(completed))
                        released.extend(completed)
                        completed = []

            print("===============")
            print(released)
            print(completed)
            print(ans)

    print("---------------------")
    return ans


cases = [
        [[93, 30, 55], [1, 30, 5]], # [2, 1]
        [[40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]], # [1, 2, 3]
        [[93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]], # [2, 4]
        ]
for case in cases:
    progresses, speeds = case
    print(solution(progresses, speeds))
