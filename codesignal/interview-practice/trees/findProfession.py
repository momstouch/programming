# https://app.codesignal.com/interview-practice/task/FwAR7koSB3uYYsqDp

def findProfession_timeout(level, pos):
    def find(pro, level, pos, tar_pos):
        if level == 1:
            if pos + 1 == tar_pos:
                return pro
            else:
                return ""
        return find(pro, level - 1, pos * 2, tar_pos) + \
                find("Doctor" if pro == "Engineer" else "Engineer",
                        level - 1, pos * 2 + 1, tar_pos)

    return find("Engineer", level, 0, pos)


def findProfession_timeout2(level, pos):
    num_q = 2 ** (level - 1) - 1 + pos

    q = ["Engineer"]

    while q:
        pro = q.pop(0)
        num_q -= 1
        if num_q == 0:
            return pro

        q.append(pro)
        q.append("Engineer" if pro == "Doctor" else "Doctor")

    return None


def findProfession_pass(level, pos):
    n = 2 ** (level - 1)
    ans = 0

    while level > 1:
        level -= 1

        n = n / 2

        if pos > n:
            ans ^= 1
            pos = pos - n

    return "Engineer" if ans == 0 else "Doctor"


# Count the number of child node on the right side of the parent 
# from the bottom to root.
# parent pos = (pos + 1) // 2 
def findProfession(level, pos):
    def fp(level, pos):
        if level == 1:
            return False

        #print(level, pos, pos % 2 != 0)
        return ((pos % 2) == 0) ^ fp(level - 1, (pos + 1) // 2)

    return "Doctor" if fp(level, pos) else "Engineer"


cases = [
        (3, 3),     # "Doctor"
        (1, 1),     # "Engineer"
        (4, 2),     # "Doctor"
        ]
for level, pos in cases:
    print(findProfession(level, pos))
