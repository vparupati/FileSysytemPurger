from multiprocessing.dummy import Pool


def match_key(mapping_tuple):
    file_name, keys_to_match = mapping_tuple
    file_name = file_name.lower()
    for key in keys_to_match:
        matched = file_name.find(key.lower())
        if matched > -1:
            return key
    return None


class MatchKeys:

    def __init__(self):
        self.p = Pool(5)

    def match_key(self, mapping_tuple):
        return next((item for item in self.p.map(match_key, mapping_tuple) if item is not None), None)

