import threading
from multiprocessing.dummy import Pool

from test.A import A


def match_key(mapping_tuple):
    file_name, keys_to_match = mapping_tuple
    file_name = file_name.lower()
    for key in keys_to_match:
        matched = file_name.find(key.lower())
        if matched > -1:
            return key
    return None


def _get_chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def _zip_keys_and_file_name(keys_list, file_name ):
    return ((file_name, key) for key in keys_list)


class KeyMatcher:

    def __init__(self,keys):
        self.key_lists = _get_chunks(keys, 500)
        self.p = Pool(10)

    def mk(self, fname):
        l =[]
        for kl in self.key_lists:
            l.append(match_key((fname, kl)))
        return l

    def match_key(self, file_name):
        #return next((item for item in self.mk(file_name) if item is not None), None)
        a = A(file_name)
        return next((item for item in self.p.map(a.mk, self.key_lists, len(self.key_lists)/8) if item is not None), None)
