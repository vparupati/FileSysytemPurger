import os
import random
import string


def _get_random_filename():
    for i in range(10):
        key = ''.join(random.choice(string.digits + string.ascii_uppercase) for x in range(8))
        name = ''.join(random.choice(string.digits + string.ascii_lowercase + '_') for x in range(15))
        return (key, "{0} {1}.txt".format(key, name))


def _file_text():
    return ''.join(random.choice(string.printable) for x in range(1000))


def generate_big_random_sentences(filename, line_count):
    import random
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")

    all = [nouns, verbs, adj, adv]

    with open(filename, 'w') as f:
        for i in range(line_count):
            f.writelines([' '.join([random.choice(i) for i in all]), '\n'])
    pass


def create_random_files_in(directory):
    key, f_name = _get_random_filename()
    keys.append(key)
    generate_big_random_sentences(directory + '/' + f_name, 100)


dir_paths = ['ch1', 'ch1/ch11', 'ch2', 'ch2/ch21']
test_fs_root = 'c:/Users/vidyasagar.parupati/testfs'
keys = []

if not os.path.exists(test_fs_root):
    os.makedirs(test_fs_root)

for path in dir_paths:
    path = test_fs_root + '/' + path
    if not os.path.exists(path):
        os.makedirs(path)
    for count in range(30000):
        create_random_files_in(path)

with open('./test_keys.csv', 'w') as kf:
    kf.write("\n".join(keys))
