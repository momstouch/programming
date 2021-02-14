# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name == b.name:
                return 0
            elif a.name > b.name:
                return 1
            else:
                return -1
        else:
            return -1


cases = [
        ([
            ["amy", 100],
            ["david", 100],
            ["heraldo", 50],
            ["aakansha", 75],
            ["aleska", 150]
            ]),
        ]
for scores in cases:
    data = []
    for name, score in scores:
        player = Player(name, int(score))
        data.append(player)

    data = sorted(data, key = cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
