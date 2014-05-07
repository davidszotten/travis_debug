# import inspect
import linecache
import sys

import mock


def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        if filename == "<stdin>":
            filename = "traceit.py"
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")):
            filename = filename[:-1]
        name = frame.f_globals["__name__"]
        f_locals = frame.f_locals
        line = linecache.getline(filename, lineno)
        left = ("%s:%s: %s" % (name, lineno, line.rstrip())).ljust(80)
        right = "%s, name: %s" % (f_locals.keys(), repr(f_locals.get('name')))
        print "%s %s" % (left, right)

        # print "%s:%s: %s (%s)" % (name, lineno, line.rstrip(), f_locals)
    return traceit


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

print
sys.settrace(traceit)
value < 0
sys.settrace(None)
print


# print "############################################################"
# print inspect.getsource(mock)
# print "############################################################"
