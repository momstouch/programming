# https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H

def isCryptSolution(crypt, solution):
    crypt_dict = {code: val for code, val in solution}

    arith_str = ""
    for s in crypt:
        for c in s:
            arith_str += crypt_dict[c]

        arith_str += ' '

    nums = []
    for num_str in arith_str[:-1].split(' '):
        if num_str[0] == '0' and len(num_str) > 1:
            return False
        nums.append(int(num_str))

    return nums[0] + nums[1] == nums[2]


def pythonic_code(crypt, solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeros = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeros and int(t[0]) + int(t[1]) == int(t[2])


cases = [
        [
            ["SEND", "MORE", "MONEY"],
            [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
            ],
        [
            ["TEN", "TWO", "ONE"],
            [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
            ],
        ]
for crypt, solution in cases:
    print(isCryptSolution(crypt, solution))
    print(pythonic_code(crypt, solution))
