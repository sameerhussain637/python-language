import os
path = "C:/Users/samee/OneDrive/Desktop/pyfol"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)