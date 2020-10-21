# https://app.codesignal.com/interview-practice/task/dYCH8sdnxGf5aGkez/description

def decodeString(s):
    ls = list(s)
    st = [ls.pop(0)]
    ans = []

    while st:
        c = st.pop()



cases = [
        "4[ab]",        # "abababab"
        "2[b3[a]]",     # "baaabaaa"
        "z1[y]zzz2[abc]",   # "zyzzzabcabc"
        ]
for s in cases:
    print(decodeString(s))
