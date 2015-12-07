import sys


def parse():
    if sys.argv <= 1:
        return None, None

    key = lambda x: x.split('=')[0]
    value = lambda x: x.split('=')[1]
    argvs = sys.argv[1:]
    args = [i for i in argvs if '=' not in i]
    kwargs = {key(i): value(i) for i in argvs if '=' in i}
    return args, kwargs
