import cv2
import os
import numpy as np
from os import listdir
from src.commons.ImgProcessing import ImgProcessing
from src.commons.SkinDetection import SkinDetection

pathDataSet = "./data/set/"
pathSkinMaskSet = "./data/skin_mask/"
pathNotSkingMaskSet = "./data/non_skin_mask/"
outputSkinModelFile = "output/skinModel.txt"
outputNonSkinModelFile = "output/nonSkinModel.txt"

# list of ground skin ground images
listOfSkinMask = listdir(pathSkinMaskSet)
print(listOfSkinMask)

# list of original images
listOfDataSet = listdir(pathDataSet)
print(listOfDataSet)

# current directory
fileDir = os.path.dirname(os.path.realpath('__file__'))


def menu():
    print("\n\n")
    print("0 TO QUIT")
    print("1 TO CREATE A NEW MODEL")
    print("2 DETECT SKIN")
    print("\n")

def main():
    menu()
    choiceList = [0, 1, 2]
    choice = input("Enter your action : ")
    while choice != 0:


        #TO CREATE A NEW MODEL
        if str(choice) == str(1):
            # Look for images and their corresponding ground image / mask
            print("Total image to learn : "+str(len(listOfDataSet)))

            for img in listOfDataSet:
                splitImg = img.split('.')
                print(splitImg)
                for ground in listOfSkinMask:
                    splitGrd = ground.split('.')

                    if splitImg[0] in splitGrd[0] and len(splitImg[0]) == len(splitGrd[0]):
                        print(img + "====" + ground)

                        IMAGE = ImgProcessing(os.path.join(fileDir, "data/set/" + img),
                                              os.path.join(fileDir, "data/skin_mask/" + ground))
                        print(IMAGE.width)
                        print(IMAGE.height)
                        IMAGE.getNonSkinPixel()
                        listNonSkinAB = IMAGE.getSetABChannelNonSkinValues()
                        fileObject = open(os.path.join(fileDir, outputNonSkinModelFile), "a+")
                        fileObject.close()
                        for ab in listNonSkinAB:
                            exist = False
                            with open(os.path.join(fileDir, outputNonSkinModelFile), "r+") as fileObject:
                                for line in fileObject:
                                    newline = line.split()
                                    print(newline)
                                    print(ab['a'])
                                    print(ab['b'])
                                    if len(newline) > 0 and str(newline[0]) == str(ab['a']) and str(newline[1] == str(ab['b'])) and str(newline[2]) == str(IMAGE.getNonSkinPixelProbabilities(ab['a'], ab['b'])):
                                        exist = True
                                        break

                            if not exist:
                                fileObject = open(os.path.join(fileDir, outputNonSkinModelFile), "a+")
                                fileObject.write(
                                    str(ab['a']) + " " + str(ab['b']) + " " + str(IMAGE.getNonSkinPixelProbabilities(ab['a'], ab['b'])))
                                fileObject.write(str("\n"))
                                fileObject.close()
                        '''
                        IMAGE.getSkinPixel()
                        listSkinAB = IMAGE.getSetABChannelSkinValues()
                        fileObject = open(os.path.join(fileDir, outputNonSkinModelFile), "a+")
                        fileObject.close()
                        for ab in listSkinAB:
                            exist = False
                            with open(os.path.join(fileDir, outputSkinModelFile), "r+") as fileObject:
                                for line in fileObject:
                                    newline = line.split()
                                    print(newline)
                                    print(ab['a'])
                                    print(ab['b'])
                                    if len(newline) > 0 and str(newline[0]) == str(ab['a']) and str(newline[1] == str(ab['b'])) and str(newline[2]) == str(IMAGE.getSkinPixelProbabilities(ab['a'], ab['b'])):
                                        exist = True
                                        break

                            if not exist:
                                fileObject.write(
                                    str(ab['a']) + " " + str(ab['b']) + " " + str(IMAGE.getSkinPixelProbabilities(ab['a'], ab['b'])))
                                fileObject.write(str("\n"))
                            fileObject.close()
                        '''

        # DETECT SKIN
        elif str(choice) == str(2):
            detection = SkinDetection("./data/set/5.jpg", os.path.join(fileDir, outputSkinModelFile), nonSkinModeFile=None)
            detection.detectSkin()
        else:
            print("\n\nUnKnown choice\n\n")

        menu()
        choice = int(input("Enter your action : "))


if __name__ == '__main__':
    main()

