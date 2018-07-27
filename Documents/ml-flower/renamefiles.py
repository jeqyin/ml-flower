import numpy
import os
import getopt
import sys
from datetime import datetime

def usage():
    print("arg[1] = source folder. Use flags -b to set base name, -n to have incrementing files, or -d to rename to creation date")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[2:], "hndb:", ["help", "number", "date","base"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    date = False
    base = ""
    sourceFolder = sys.argv[1]

    for o, a in opts:
        if o == "-n":
            date = False
        elif o=="-d":
            date = True
        elif o == "-b":
            base = a
        else:
            assert False, "unhandled option"

    while True:
        if os.path.isdir(sourceFolder):
            break
        else:
            print("Folder doesn't exist. Input another.")
            sourceFolder = input("Input folder: ")
            type(sourceFolder)
      
    i = 0
    dates = dict()

    for fileName in os.listdir(sourceFolder):
        if date:
            sortMeth = datetime.fromtimestamp(os.path.getctime(sourceFolder + fileName)).strftime('%Y_%m_%d')
            if sortMeth in dates:
                dates[sortMeth]+=1
                sortMeth += "(" + str(dates[sortMeth]) + ")"
            else:
                dates[sortMeth] = 0
        else:
            sortMeth = str(i)
        os.rename(sourceFolder+fileName, sourceFolder + base + sortMeth + "." + fileName.split('.')[1])
        i+=1

if __name__ == "__main__":
    main()