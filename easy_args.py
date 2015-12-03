import sys


def args(func):
    def func_wrapper(*args, **kwargs):
        all_args = list(args) + sys.argv[1:]
        new_args = filter(lambda x: x.find('=') == -1, all_args)
        new_kwargs = {
            x.split('=')[0]: x.split('=')[1]
            for x in list(set(all_args) - set(new_args))}
        return func(*new_args, **new_kwargs)
    return func_wrapper


def args_inject(func):
    def func_wrapper(*args, **kwargs):
        all_args = list(args) + sys.argv[1:]
        new_args = filter(lambda x: x.find('=') == -1, all_args)
        new_kwargs = {
            x.split('=')[0]: x.split('=')[1]
            for x in list(set(all_args) - set(new_args))}
        for k, v in new_kwargs.items():
            func.func_globals[k] = v
        return func()
    return func_wrapper
