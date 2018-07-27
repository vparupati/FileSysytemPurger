import csv
import os
import time


def move_files():
    with open('./fileTobDeleted.csv') as fileList:
        reader = csv.DictReader(fileList)
        for row in reader:
            try:
                os.remove(row['path'])
            except OSError as err:
                #write to erro file
                print(err.__cause__)
                pass


start = time.time()
move_files()
end = time.time()
print("\n")
print("Time to execute : {0} sec".format(end - start))
