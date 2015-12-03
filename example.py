from easy_args import args, args_inject


@args
def foo(*args, **kwargs):
    name = kwargs['name']
    lastname = kwargs['lastname']
    print(args)
    print(name + ' ' + lastname)


@args_inject('name')
def name():
    print('Your name is:')
    print(name)  # noqa


if __name__ == '__main__':
    foo()
    name()
