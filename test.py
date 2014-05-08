from mock import MagicMock

m1 = MagicMock()

print m1 < 0

print type(m1) < type(0)

print type(m1) is MagicMock
print isinstance(m1, MagicMock)
print MagicMock < int


class Foo(object):
    pass

class foo(object):
    pass

class bar(object):
    pass

class Bar(object):
    pass

print "types"
print "Foo defined before foo"
print "Bar defined after bar"

print "Foo < foo:", Foo < foo
print "Bar < bar:", Bar < bar
