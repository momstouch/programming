# https://app.codesignal.com/interview-practice/task/dYCH8sdnxGf5aGkez/description

def decodeString(s):
    def decode(s):
        ans = ""

        while s:
            c = s.pop(0)

            if c.isalpha():
                ans += c
            elif c.isdigit():
                cnt = c
                while True:
                    cc = s.pop(0)
                    if cc == '[': break
                    cnt += cc
                ans += decode(s) * int(cnt)
            else:
                return ans

        return ans

    return decode(list(s))


cases = [
        "4[ab]",        # "abababab"
        "2[b3[a]]",     # "baaabaaa"
        "z1[y]zzz2[abc]",   # "zyzzzabcabc"
        ]
for s in cases:
    print(decodeString(s))
