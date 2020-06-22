from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    print(answer.keys())
    return list(answer.keys()).pop()

case = {}
case[0] = [
        ["leo", "kiki", "eden"], ["eden", "kiki"]
        ] # answer: leo
case[1] = [
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"]
        ] # answer: vinko
case[2] = [
        ["mislav", "stanko", "mislav", "ana"],
        ["stanko", "ana", "mislav"]
        ] # answer: mislav

for c in case:
    part, comp = case[c]
    print(solution(part, comp))
