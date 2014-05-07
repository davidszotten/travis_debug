import inspect

import mock


def display(value):
    print value
    print repr(value)
    print

dict_map = mock.MagicMock()
display(dict_map)

value = dict_map.get('value')
display(value)


print value < 0
print value == 0
print value > 0

print "############################################################"
print inspect.getsource(mock)
print "############################################################"
