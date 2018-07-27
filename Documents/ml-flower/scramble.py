import numpy as np
import os
import sys
import random
from PIL import Image

default = "sample/"

def scramble():

    if len(sys.argv) != 3 or not os.path.isdir(sys.argv[1]):
        print("usage: cmd <source folder> <output folder>")
        sys.exit(1)

    sourceFolder = sys.argv[1]
    outFolder = sys.argv[2]
    os.makedirs(outFolder, exist_ok=True)

    for fileName in os.listdir(sourceFolder):
        f = Image.open(sourceFolder + '/' + fileName)
        mat = np.array(f)
        for i in range(mat.shape[0]):
            random.shuffle(mat[i])
        random.shuffle(mat)
        im = Image.fromarray(mat)
        im.save(outFolder + '/' + fileName)

if __name__ == "__main__":
    scramble()