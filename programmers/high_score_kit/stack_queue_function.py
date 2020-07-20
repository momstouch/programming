# https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    ans = []

    released = 0

    while progresses:
        progresses = [p + s for p, s in zip(progresses, speeds)]
        indices = [i for i, progress in enumerate(progresses) if progress >= 100]
        release = [index for i, index in enumerate(indices) if index == i]

        if release:
            progresses = progresses[release[-1] + 1: ]
            speeds = speeds[release[-1] + 1: ]
            ans.append(len(release))

    return ans


# best solution ever
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1

    print("q", Q)
    return [q[1] for q in Q]


cases = [
        [[93, 30, 55], [1, 30, 5]], # [2, 1]
        [[40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]], # [1, 2, 3]
        [[93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]], # [2, 4]
        ]
for progresses, speeds in cases:
    print(solution(progresses, speeds))
    #print(solution2(progresses, speeds))
