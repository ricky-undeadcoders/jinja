from jinja2._compat import imap, string_types, text_type, iteritems, PY2
from jinja2.exceptions import FilterArgumentError


def do_reverse(value):
    """Reverse the object or return an iterator that iterates over it the other
    way round.
    """
    if isinstance(value, string_types):
        return value[::-1]
    try:
        print('first forward len', len(value))
        print(type(value))
        print(type(reversed(value)))
        return reversed(value)
    except TypeError:
        try:
            rv = list(value)
            print('forward len', len(rv))
            rv.reverse()
            print('reverse len', len(rv))
            return rv
        except TypeError:
            raise FilterArgumentError('argument must be iterable')


this = do_reverse([10, 9])
print(len(this))

for that in this:
    print(that)
