from multiprocessing.pool import Pool

from MatchKeys import MatchKeys


def f(x):
    return x * x


def match_key(mapping_tuple):
    file_name, keys_to_match = mapping_tuple
    file_name = file_name.lower()
    for key in keys_to_match:
        matched = file_name.find(key.lower())
        if matched > -1:
            return key
    return None


lis = [1, 2, 3, 4, 5, 435, 54, 6, 67, 7, 878, 7, 8, 78, 789, 78, 978, 9, 56, 980, 98, 56, 89, 89, 78, 8, 78, 67, 6, 7,
       678, 67, 87, 8, 78, 78, 978, 9, 78, 978, 546, 879, 78, 978, 9, 789, 78, 78, 9, 78, 978, 9, 789, 78, 9, 789, 789,
       78, 978, 9789, 789, 78, 978, 9, 98, 98, 89, 45, 890, 89, 4]


def _get_chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def _get_as_tuples(k, chunks):
    tuples = []
    for ch in chunks:
        tuples.append((k, ch))
    return tuples


def a():
    p = Pool(5)
    print(p.map(match_key, [('asdasssssss', ['asdas', 'ewsvds', 'rtsde', 'rtrvsd']),
                            ('asdasssssss', ['asdasd', 'ewfdaw', 'rfsssw']),
                            ('asdasssssss', ['asdasda', 'ewrds', 'fewdfsd', 'serwe'])]))


# print(_get_as_tuples('as', _get_chunks(lis, 5)))

matchKeys = MatchKeys()
print(matchKeys.match_key([('asdasssssss', ['asdas', 'ewsvds', 'rtsde', 'rtrvsd']),
                           ('asdasssssss', ['asdasd', 'ewfdaw', 'rfsssw']),
                           ('asdasssssss', ['asdasda', 'ewrds', 'fewdfsd', 'serwe'])]))
print(matchKeys.match_key([('asdasssssss', ['asdas', 'ewsvds', 'rtsde', 'rtrvsd']),
                           ('asdasssssss', ['asdasd', 'ewfdaw', 'rfsssw']),
                           ('asdasssssss', ['asdasda', 'ewrds', 'fewdfsd', 'serwe'])]))
print(matchKeys.match_key([('asdasssssss', ['asdas', 'ewsvds', 'rtsde', 'rtrvsd']),
                           ('asdasssssss', ['asdasd', 'ewfdaw', 'rfsssw']),
                           ('asdasssssss', ['asdasda', 'ewrds', 'fewdfsd', 'serwe'])]))
print(matchKeys.match_key([('ffsdasssssss', ['asdas', 'ewsvds', 'rtsde', 'rtrvsd']),
                           ('ffsdasssssss', ['asdasd', 'ewfdaw', 'rfsssw']),
                           ('ffdasssssss', ['asdasda', 'ewrds', 'fewdfsd', 'serwe'])]))
