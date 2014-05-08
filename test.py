from mock import Mock, MagicMock

m1 = Mock()

m4 = MagicMock()
m5 = MagicMock()
m5.__lt__.return_value = NotImplemented
m6 = MagicMock()
m6.__lt__.side_effect = lambda x: NotImplemented


class Foo(object):
    def __lt__(self, other):
        return NotImplemented


foo = Foo()

m7 = Mock(wraps=foo)
m8 = MagicMock(wraps=foo)

print 1, m1 < 0
print 4, m4 < 0
print 5, m5 < 0
print 6, m6 < 0
print 7, m7 < 0
print 8, m8 < 0

print 'f', foo < 0
