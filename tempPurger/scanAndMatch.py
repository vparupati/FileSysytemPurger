import csv
import os
import time

import myconfig


def scan_filesystem(path, keys_to_match, files_found):
    count = 0
    try:
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                count += scan_filesystem(entry.path, keys_to_match, files_found)
            else:
                matched_key = match_key(entry.name, keys_to_match)
                if matched_key is not None:
                    files_found.append((matched_key, entry.name, entry.path))
                count += 1
    except PermissionError as err:
        print("Access Error error: {0}".format(err))
    except OSError as err:
        print("OS Error error: {0}".format(err))
    return count


def match_key(file_name, keys_to_match):
    file_name = file_name.lower()
    for key in keys_to_match:
        matched = file_name.find(key.lower())
        if matched > -1:
            return key
    return None


def match_key(mapping_tuple):
    file_name, keys_to_match = mapping_tuple
    file_name = file_name.lower()
    for key in keys_to_match:
        matched = file_name.find(key.lower())
        if matched > -1:
            return key
    return None


def _read_primary_keys(path):
    with open(path) as pks:
        return pks.read().splitlines()


files_found = []

start = time.time()
fileScanned = scan_filesystem(myconfig.source_to_scan, _read_primary_keys(myconfig.keys_location),
                              files_found)
end = time.time()
print("\n")
print("Time to execute : {0} sec".format(end - start))
print("Files scanned : {0}".format(fileScanned))
print("Files found : {0}".format(len(files_found)))
print("\n")
with open(myconfig.tobe_deleted_preview, 'w') as csvfile:
    fieldnames = ['Reference', 'file', 'path']
    writer = csv.writer(csvfile)
    writer.writerow(['Reference', 'file', 'path'])
    for file in files_found:
        writer.writerow(file)
