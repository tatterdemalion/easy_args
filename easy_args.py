import sys
import functools


def parse():
    if sys.argv <= 1:
        return None, None

    key = lambda x: x.split('=')[0]
    value = lambda x: x.split('=')[1]
    argvs = sys.argv[1:]
    args = [i for i in argvs if '=' not in i]
    kwargs = {key(i): value(i) for i in argvs if '=' in i}
    return args, kwargs


def args(func):
    def wrapper(*args, **kwargs):
        new_args, new_kwargs = parse(*args, **kwargs)
        return func(*new_args, **new_kwargs)
    return wrapper


def args_inject(*keys):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_args, new_kwargs = parse()
            if keys:
                for k in keys:
                    func.func_globals[k] = new_kwargs[k]
            else:
                for k, v in new_kwargs.items():
                    func.func_globals[k] = v
            return func(*args, **kwargs)
        return wrapper
    return decorator
