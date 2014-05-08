from mock import MagicMock

m1 = MagicMock()

def print_and_return(*args, **kwargs):
    print args, kwargs
    return NotImplemented

m1.__lt__.side_effect = print_and_return
m1.__gt__.side_effect = print_and_return


print m1 < 0

print object.__getattribute__(m1, '__lt__')(0)
