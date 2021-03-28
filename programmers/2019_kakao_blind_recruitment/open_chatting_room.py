# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    id_nick = {}
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for re in record:
        re = re.split(' ')
        action, _id = re[:2]

        if action == "Enter" or action == "Change":
            id_nick[_id] = re[-1]

    result = []
    for re in record:
        re = re.split(' ')
        if re[0] in printer:
            result.append(id_nick[re[1]] + printer[re[0]])

    return result

cases = [
        (["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"],
            ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]),
        ]

for record, answer in cases:
    assert solution(record) == answer
