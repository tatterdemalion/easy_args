[![Build Status](https://travis-ci.org/tatterdemalion/easy_args.svg?branch=master)](https://travis-ci.org/tatterdemalion/easy_args)

```
from easy_args import args_inject

@args_inject()
def foo():
    print(name + ' ' + lastname)

foo()
```

```
$ python example.py name=John lastname=Doe

John Doe
```

# What is this?
easy_args injects system parameters to function scope.

# Why?
Because i was trying to find an easy way to get named parameters like ```name=John``` with lesser effort. All the other solutions, including ```argparse``` are way to complicated for basic usage.

# When should I use it?
When you do not really need to design a CLI application but a simple script with some parameters. ```easy_args``` does not support docs and help strings, does not validate parameters, does not raise sensible errors for missing parameters and probably never will. Also, use it with caution. We are actually injecting stuff into function scope here. Make sure the decorated functions are isolated from outside world.

# Installation
```
pip install easy_args
```

# Examples:

## By using positional and keyword arguments

```
from easy_args import args

@args
def foo(*args, **kwargs):
    name = kwargs['name']
    lastname = kwargs['lastname']
    print(args)
    print(name + ' ' + lastname)

foo()
```

```
$ python example.py your name is name=John lastname=Doe

('your', 'name', 'is')
John Doe
```

## By injecting keyword arguments to the function scope (As the example above)

```
from easy_args import args_inject

@args_inject()
def foo():
    print(name + ' ' + lastname)

foo()
```

```
$ python example.py name=John lastname=Doe

John Doe
```

You can also restrict required variables by function:

```
from easy_args import args_inject

@args_inject('name', 'times')
def foo():
    for i in range(int(times)):
        print(name)  # using lastname in this scope will raise a NameError here.

foo()
```

```
$ python example.py name=John lastname=Doe times=4

John
John
John
John
```

## By using with statement

```
from easy_args import args_get

with args_get() as a:
    print(a.name + ' ' + a.lastname)
```

```
python example.py name=John lastname=Doe

John Doe
```

