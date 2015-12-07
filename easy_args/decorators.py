import functools
from .parsers import parse


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
