from .parsers import parse


class ArgsGet(object):
    def __enter__(self):
        self.args, self.kwargs = parse()
        for name, value in self.kwargs.items():
            setattr(self, name, value)
        return self

    def __exit__(self, _type, value, traceback):
        del self.args
        for name in self.kwargs.keys():
            delattr(self, name)
        del self.kwargs


args_get = ArgsGet
