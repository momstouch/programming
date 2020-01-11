# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    participant.sort()
    comp = sorted(completion) + [""]

    for p, c in zip(participant, comp):
        if p != c:
            return p


def solution2(participant, completion):
    c_dict = {}
    for c in completion:
        c_dict[c] = None

    for p in participant:
        if p not in c_dict:
            return p
        else:
            c_dict.pop(p)


from collections import Counter
def solution3(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys()).pop()


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
# return "leo"

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
# return "vinko"


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# return "mislav"
print(solution(participant, completion))
print(solution2(participant, completion))
print(solution3(participant, completion))
