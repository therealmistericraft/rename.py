import os
from os import listdir
from os.path improt isfile, join

removal = "IMG_"
path = "/"
files = [f for f in listdir(path) if isfile(join(path, f)]
nFiles = []

i=0
while i != files.len():
    nFile = files[i].replace(removal, "")
    os.rename(files[i], nFile)
    i++
