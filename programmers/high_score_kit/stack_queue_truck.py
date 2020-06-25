# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    sec = 0
    on_bridge = {}
    after_brg = []
    weight_on_brg = []
    n_trucks = len(truck_weights)
    while len(after_brg) < n_trucks:
        for i in on_bridge:
            on_bridge[i] += 1
            if on_bridge[i] > bridge_length and not i in after_brg:
                after_brg.append(i)
                weight_on_brg.pop(0)

        if truck_weights:
            if sum(weight_on_brg + [truck_weights[0]]) < weight:
                weight_on_brg.append(truck_weights.pop(0))
                on_bridge[sec] = 1

        sec += 1

    answer = sec
    return answer


cases = [
        #[2, 10, [7, 4, 5, 6]],                             # 8
        #[100, 100, [10]],                               # 101
        [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],   # 110
        ]

for case in cases:
    bridge_length, weight, truck_weights = case
    print(solution(bridge_length, weight, truck_weights))
