from easy_args import args_inject


@args_inject
def hello():
    print('Your name is:')
    print(name + ' ' + lastname)

hello()
