# https://app.codesignal.com/interview-practice/task/HdgqPhHqs3NciAHqH/description

def countClouds(skyMap):
    def clean(skyMap, x, y):
        if skyMap[x][y] == '1':
            skyMap[x][y] = '0'

            if y + 1 < len(skyMap[x]):
                clean(skyMap, x, y + 1)
            if y > 0:
                clean(skyMap, x, y - 1)
            if x + 1 < len(skyMap):
                clean(skyMap, x + 1, y)
            if x > 0:
                clean(skyMap, x - 1, y)

    ans = 0
    for x, r in enumerate(skyMap):
        for y, c in enumerate(r):
            if c == '1':
                ans += 1
                clean(skyMap, x, y)

    return ans


cases = [
        [['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']],       # 2
        [['0', '1', '0', '0', '1'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '1'],
          ['0', '0', '1', '1', '0'],
          ['1', '0', '1', '1', '0']],       # 5
        ]
for skyMap in cases:
    print(countClouds(skyMap))
