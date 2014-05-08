from mock import MagicMock

m1 = MagicMock()

print m1 < 0

print type(m1) < type(0)

print type(m1) is MagicMock
print isinstance(m1, MagicMock)
print MagicMock < int
