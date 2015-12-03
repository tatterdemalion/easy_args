import sys
import functools


def parse(*args, **kwargs):
    if sys.argv <= 1:
        return None, None
    all_args = list(args) + sys.argv[1:]
    new_args = filter(lambda x: x.find('=') == -1, all_args)
    new_kwargs = {
        x.split('=')[0]: x.split('=')[1]
        for x in list(set(all_args) - set(new_args))}
    return new_args, new_kwargs


def args(func):
    def wrapper(*args, **kwargs):
        new_args, new_kwargs = parse(*args, **kwargs)
        return func(*new_args, **new_kwargs)
    return wrapper


def args_inject(*keys):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_args, new_kwargs = parse(*args, **kwargs)
            if keys:
                for k in keys:
                    func.func_globals[k] = new_kwargs[k]
            else:
                for k, v in new_kwargs.items():
                    func.func_globals[k] = v
            return func(*args, **kwargs)
        return wrapper
    return decorator
