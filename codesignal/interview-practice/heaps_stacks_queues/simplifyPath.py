# https://app.codesignal.com/interview-practice/task/aRwxhGcmvhf6vKPCp/description

def simplifyPath(path):
    stack = []
    for directory in path.split('/'):
        if directory:
            if directory == '.':
                pass
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

    return '/' + '/'.join(stack)

cases = [
        "/home/a/./x/../b//c/",     # "/home/a/b/c"
        ]
for path in cases:
    print(simplifyPath(path))
