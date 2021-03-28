# https://programmers.co.kr/learn/courses/30/lessons/17685

class Node(object):
    def __init__(self, value):
        self.c = value
        self.next = {}
        self.ref = 1

    def set_next(self, value):
        try:
            next_node = self.next[value]
        except KeyError:
            next_node = Node(value)
            self.next[value] = next_node

        return next_node

def find_word(root, word, count = 0):
    if not root or not word or not word[0] in root:
        return count

    if root[word[0]].ref == 1:
        return count + 1

    return find_word(root[word[0]].next, word[1:], count + 1)

def solution(words):
    root = {}
    for word in words:
        try:
            node = root[word[0]]
            node.ref += 1
        except KeyError:
            node = root[word[0]] = Node(word[0])

        for i, ch in enumerate(word[1:], start = 1):
            try:
                node = node.next[ch]
                node.ref += 1
            except KeyError:
                node = node.set_next(ch)

    answer = 0
    for word in words:
        answer += find_word(root, word)

    return answer

cases = [
        (["go","gone","guild"], 7),
        (["abc","def","ghi","jklm"], 4),
        (["word","war","warrior","world"], 15),
        ]
for words, answer in cases:
    assert solution(words) == answer
