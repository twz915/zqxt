VERSION = (0, 0, '2b')


def get_version():
    return '.'.join([str(v) for v in VERSION])


__version__ = get_version()
