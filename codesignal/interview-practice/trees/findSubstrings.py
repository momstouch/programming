# https://app.codesignal.com/interview-practice/task/Ki9zRh5bfRhH6oBau

# brute force
def findSubstrings_timeout(words, parts):
    dic = {}
    for w in words:
        for p in parts:
            if p in w:
                old = dic.get(w, "")
                lp = len(p)
                lo = len(old)
                if lp > lo:
                    dic[w] = p
                elif lp == lo and w.index(p) < w.index(old):
                    dic[w] = p

    ans = []
    for w in words:
        p = dic.get(w, None)
        if p is None:
            ans.append(w)
        else:
            ans.append(w.replace(p, "[%s]" % (p), 1))

    return ans


class Node(object):
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.end = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return cur.end

# using Trie
def findSubstrings(words, parts):
    trie = Trie()
    for p in parts:
        trie.insert(p)

    part_lengs = sorted(set([len(p) for p in parts]), reverse = True)

    for i in range(len(words)):
        word = words[i]
        findflag = False

        for p in part_lengs:
            for j in range(len(word) - p + 1):
                if trie.search(word[j:j + p]):
                    words[i] = word.replace(word[j:j + p], "[%s]" % (word[j:j + p]), 1)
                    findflag = True
                    break

            if findflag:
                break

    return words


cases = [
        (
            ["Apple", "Melon", "Orange", "Watermelon"],
            ["a", "mel", "lon", "el", "An"]
            ), # ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"]
        ]
for words, parts in cases:
    print(findSubstrings(words, parts))
