# easy_args
get system args easily

# example:

```
# emample.py
from easy_args import args_inject


@args_inject
def hello():
    print('Your name is:')
    print(name + ' ' + lastname)

hello()
```

```
$ python example.py name=John lastname=Doe

Your name is:
John Doe
```
