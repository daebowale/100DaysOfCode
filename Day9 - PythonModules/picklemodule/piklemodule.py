# pickle module in Python

# pickle is a build in module of python

import pickle

# Firtsly, let's Pickling a Python object

# cars = ["AUDI", "TESLA", "FERRARI", "MARUTI SUZUKI", "NANO"]

# .pkl file is in binary object format. You cannot open this file and You cannot read it in text format!

# file = "mycars.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars, fileobj)
# fileobj.close()


# Depickling the mycar.pkl file

file2 = "mycars.pkl"
fileobj2 = open(file2, "rb")
mycars2 = pickle.load(fileobj2)
print(mycars2)
print(type(mycars2))
fileobj2.close()
