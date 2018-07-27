import multiprocessing
from itertools import product


def merge_names(a, b):
    return '{} & {}'.format(a, b)


if __name__ == '__main__':
    for a in product('ab', repeat=2):
        print(a)

    names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
    print(product(names, repeat=2))
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(merge_names, product(names, repeat=2))
    print(results)
