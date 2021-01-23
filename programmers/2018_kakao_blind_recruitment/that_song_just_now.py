#https://programmers.co.kr/learn/courses/30/lessons/17683

def get_time_difference(begin: str, end: str) -> int:
    begin_h, begin_m = begin.split(":")
    end_h, end_m = end.split(":")

    begin_h = int(begin_h)
    begin_m = int(begin_m)
    end_h = int(end_h)
    end_m = int(end_m)

    if end_m < begin_m:
        end_m + 60
        end_h - 1

    diff_m = end_m - begin_m
    diff_h = end_h - begin_h

    return diff_h * 60 + diff_m


def get_code_list(code: str) -> list:
    code_list = []
    for c in code:
        if c != "#":
            code_list.append(c)
        else:
            code_list[-1] = code_list[-1].lower()

    return code_list


def solution(m, musicinfos):
    answer = "(None)"
    max_tleng = -1

    m = "".join(c for c in get_code_list(m))

    for infos in musicinfos:
        begin, end, title, code = infos.split(",")
        code = get_code_list(code)

        tleng = get_time_difference(begin, end)
        mleng = len(code)

        actual_code = ""
        if mleng > tleng:
            actual_code = code[:tleng]
        else:
            ncycle = tleng // mleng
            remain = tleng % mleng
            actual_code = code * ncycle + code[:remain]


        if m in "".join(c for c in actual_code):
            if max_tleng < tleng:
                max_tleng = tleng
                answer = title

    return answer


cases = [
        (
            "ABCDEFG",
            ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
            "HELLO"
            ),
        (
            "CC#BCC#BCC#BCC#B",
            ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
            "FOO"
            ),
        (
            "ABC",
            ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"],
            "WORLD"
            )
        ]
for m, musicinfos, answer in cases:
    assert solution(m, musicinfos) == answer
