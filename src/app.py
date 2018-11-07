import cv2
import numpy as np
from os import listdir
from src.commons.ImgProcessing import ImgProcessing

pathDataSet = "./data/set/"
pathSkinMaskSet = "./data/skin_mask/"
pathNotSkingMaskSet = "./data/non_skin_mask/"

listOfSkinMask = listdir(pathSkinMaskSet)
listOfDataSet = listdir(pathDataSet)

if len(listOfDataSet) == len(listOfSkinMask):
    for mask in listOfSkinMask:
        ImageLab = ImgProcessing(mask)
        x, y = ImageLab.shape
        l, a, b = cv2.split(ImageLab)
        for i in range(x):
            for j in range(y):






