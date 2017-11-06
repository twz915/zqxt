import os.path

from django.core.cache import cache


def load_strings_from_file(cache_key, file_name):
    CACHE_TIMEOUT = 86400
    agents = cache.get(cache_key)

    if agents:
        # we got something, we are done, send it back.
        return agents

    # it wasn't in the cache, get it from the file, then store in the cache
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        ss = f.read().splitlines()

    agents = [s.strip() for s in ss if s and not s.startswith('#')]
    # store to the cache
    cache.set(cache_key, agents, CACHE_TIMEOUT)
    return agents


search_strings = load_strings_from_file('MOBI_USER_AGENT',
                                        'search_strings.txt')


def load_tablet_strings():
    return load_strings_from_file('MOBI_TABLE_USER_AGENT',
                                  'tablet_strings.txt')
