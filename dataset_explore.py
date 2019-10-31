import os, sys, path
import cv2
from collections import defaultdict

Datasets = [os.path.join("Train Images", "Large"),  os.path.join("Train Images", "Small"),
            os.path.join("Test Images")]


def imageSizesHist(path):
    d = defaultdict(int)
    cnt = 1
    size = len(os.listdir(path))
    x, step = 0.1, 0.1
    print(path)
    for item in os.listdir(path):
        img = cv2.imread(os.path.join(path, item))
        d[img.shape] += 1
        if cnt / size > x:
            print(x * 100, "%")
            x += step

        cnt += 1
    return d

def makeHistograms(filename, datsetsFolders):
    f = open(filename, 'w')
    for folder in datsetsFolders:
        dic = imageSizesHist(folder)
        f.write(str(folder) + "\n")
        for k,v in dic.items():
            f.write(str(k) + "," + str(v) + "\n")
        f.write("*"*32  +"\n")

makeHistograms("hist.txt", Datasets)
