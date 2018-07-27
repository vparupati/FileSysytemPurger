import os
import time


def get_tree(path):
    count = 0
    try:
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                count += get_tree(entry.path)
            else:
                print(entry.path)
                count += 1
    except PermissionError as err:
        print("Access Error error: {0}".format(err))
    except OSError as err:
        print("OS Error error: {0}".format(err))
    return count


start = time.time()
print(get_tree("//jhbcdffp01/CLADMIN"))
end = time.time()
print(end - start)


def get_matched_tree():

    return
