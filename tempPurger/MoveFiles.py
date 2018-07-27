import csv
import shutil
import time


def move_files():
    with open('./fileTobDeleted.csv') as fileList:
        reader = csv.DictReader(fileList)
        for row in reader:
            shutil.copy(row['path'], 'c:/Users/vidyasagar.parupati/moved')
            #shutil.move(row['path'], '//jhbcdffp01/CLADMIN/moved')


start = time.time()
move_files()
end = time.time()
print("\n")
print("Time to execute : {0} sec".format(end - start))
