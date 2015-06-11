from pandas import *
import numpy as np
import pdb
import os

def list_files(path):
    # returns a list of names (with extension, without full path) of all files
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

csv_dir = "C:\Users\mmt5267\Documents\csv_sample"
csv_files = list_files(csv_dir)

for csv_file in csv_files:
    data =  read_csv(os.path.join(csv_dir, csv_file))
    print data