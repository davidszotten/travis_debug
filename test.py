from mock import MagicMock


def display(value):
    print value
    print repr(value)
    print

dict_map = MagicMock()
display(dict_map)

value = dict_map.get('value')
display(value)


print value < 0
print value == 0
print value > 0
