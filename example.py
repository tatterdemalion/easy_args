from easy_args import args, args_inject


@args
def foo(*args, **kwargs):
    name = kwargs['name']
    lastname = kwargs['lastname']
    print(args)
    print(name + ' ' + lastname)


@args_inject()
def bar(arg_test, kwarg_test=None):
    print(arg_test)
    print(kwarg_test)
    print('Your name is:')
    print(name + ' ' + lastname)  # noqa


if __name__ == '__main__':
    foo()
    bar('hello', kwarg_test='howdie')
