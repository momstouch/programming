from collections import Counter

def solution(str1, str2):
    c1 = Counter([(i + j).lower() for i, j in zip(str1[:-1], str1[1:]) \
            if i.isalpha() and j.isalpha()])
    c2 = Counter([(i + j).lower() for i, j in zip(str2[:-1], str2[1:]) \
            if i.isalpha() and j.isalpha()])

    union = sum((c1 | c2).values())
    inter = sum((c1 & c2).values())

    if union == 0:
        inter = union = 1

    return int(65536 * (inter / union))

cases = [
        ("FRANCE", "french", 16384),
        ("aa1+aa2", "AAAA12", 43690),
        ("E=M*C^2", "e=m*c^2", 65536),
        ]
for str1, str2, ans in cases:
    assert solution(str1, str2) == ans
