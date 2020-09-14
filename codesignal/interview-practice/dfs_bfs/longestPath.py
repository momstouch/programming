# https://app.codesignal.com/interview-practice/task/iXJRYae6TBqc4ymFg

def dfs(fs, s = 0):
    if not fs:
        return 0

    cur_dep = fs[0].count('\t')

    if '.' in fs[0]:
        return s + len(fs[0]) - cur_dep

    ans = 0
    for i in range(1, len(fs)):
        new_dep = fs[i].count('\t')
        if new_dep == 0:
            return max(ans, dfs(fs[i:], 0))
        if new_dep == cur_dep + 1:
            ans = max(ans, dfs(fs[i:], s + len(fs[0]) - cur_dep + 1))
        elif new_dep <= cur_dep:
            return ans

    return ans


def longestPath(fileSystem):
    fileSystem = fileSystem.replace("    ", '\t')
    fs = fileSystem.split('\f')
    return dfs(fs, 0)


def longestPath_known_solution(fileSystem):
    answer = 0
    path_len = {0: 0}
    fs = fileSystem.replace("    ", '\t')
    for path in fs.split('\f'):
        depth = path.count('\t')
        if '.' in path:
            answer = max(answer, path_len[depth] + len(path) - depth)
        else:
            path_len[depth + 1] = path_len[depth] + len(path) - depth + 1

    return answer


cases = [
        "user\f\tpictures\f\tdocuments\f\t\tnotes.txt",     # 24
        "user\f\tpictures\f\t\tphoto.png\f\t\tcamera\f\tdocuments\f\t\tlectures\f\t\t\tnotes.txt",  # 33                                      
        "dir\f    file.txt",                                # 12
        "a\f\tb\f\t\tc.txt\fd\f\te\f\t\tfg.txt",            # 10
        "a\f\tb\f\t\tc\f\t\t\td\f\t\t\t\te.txt\f\t\t\t\talsdkjf.txt\f\t\tskdjfl.txtlsdkjflsdjflsajdflkjasklfjkasljfklas\f\tlskdjflkajsflj.txt",                     # 50
        "sladjf\f\tlkjlkv\f\t\tlkjlakjlert\f\t\t\tlaskjglaksjf\f\t\t\t\tlakjgfljrtlj\f\t\t\t\t\tlskajflakjsvlj\f\t\t\t\t\t\tlskgjflkjrtlrjt\f\t\t\t\t\t\t\tlkjglkjlvkjdlvkj\f\t\t\t\t\t\t\t\tlfjkglkjfljdlv\f\t\t\t\t\t\t\t\t\tlkdfjglerjtkrjkljsd.lkvjlkajlfk\f\t\t\t\t\t\t\tlskfjlksjljslvjxjlvkzjljajoiwjejlskjslfj.slkjflskjldfkjoietruioskljfkljf\f\t\t\t\t\tlkasjfljsaljlxkcjzljvl.asljlksaj\f\t\t\t\tasldjflksajf\f\t\t\t\talskjflkasjlvkja\f\t\t\t\twioeuoiwutrljsgfjlskfg\f\t\t\t\taslkjvlksjvlkjsflgj\f\t\t\t\t\tlkvnlksfgk.salfkjaslfjskljfv\f\t\t\tlksdjflsajlkfj\f\t\t\tlasjflaskjlk\f\t\tlsakjflkasjfkljas\f\t\tlskjvljvlkjlsjfkgljfg\f\tsaljkglksajvlkjvkljlkjvksdj\f\tlsakjglksajkvjlkjdklvj\f\tlskjflksjglkdjbkljdbkjslkj\f\t\tlkjglkfjkljsdflj\f\t\t\tlskjfglkjdfgkljsdflj\f\t\t\t\tlkfjglksdjlkjbsdlkjbk\f\t\t\t\t\tlkfgjlejrtljkljsdflgjl\f\t\t\t\t\tsalgkfjlksfjgkljsgfjl\f\t\t\t\t\tsalkflajwoieu\f\t\t\t\t\t\tlaskjfglsjfgljkkvjsdlkjbklds\f\t\t\t\t\t\t\tlasjglriotuojgkjsldfgjsklfgjl\f\t\t\t\t\t\t\t\tlkajglkjskljsdljblkdfjblfjlbjs\f\t\t\t\t\t\t\t\t\tlkajgljroituksfglkjslkjgoi\f\t\t\t\t\t\t\t\t\t\tlkjglkjkljkljdkbljsdfljgklfdj\f\t\t\t\t\t\t\t\t\t\t\tlkjlgkjljgslkdkldjblkj\f\t\t\t\t\t\t\t\t\t\t\t\tlkjfglkjlkjbsdklj.slgfjalksjglkfjglf\f\t\t\t\t\t\t\t\t\t\t\t\tlkasjrlkjwlrjljsl\f\t\t\t\t\t\t\t\t\t\t\t\t\tlksjgflkjfklgjljbljls\f\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjsglkjlkjfkljdklbjkldf\f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjglkjdlsfjdglsdjgjlxljjlrjsgjsjlk\f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjsgkllksjfgjljdslfkjlkasjdflkjxcljvlkjsgkljsfg\f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlaskjlkjsakljglsdjfgksdjlkgjdlskjb\f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkajsgfljfklgjlkdjgfklsdjklj\f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjfglkjlkgjlkjl.aslkjflasjlajglkjaf\f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjasflgjlskjglkfjgklgsdjflkbjsdklfjskldfjgklsfdjgklfdjgl\f\tlskadjlkjsldwwwwwfj\f\t\tlkjflkasjlfjlkjajslfkjlasjkdlfjlaskjalvwwwwwwwwwwwwwwwkjlsjfglkjalsjgflkjaljlkdsjslbjsljksldjlsjdlkjljvblkjlkajfljgasljfkajgfljfjgldjblkjsdljgsldjg.skljf", # 528
        ]
for case in cases:
    print(longestPath(case))
    #print(longestPath_known_in_world(case))
