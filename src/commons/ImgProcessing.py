import cv2
import numpy as np
"""
    Image processing class 
"""
class ImgProcessing:
    listOfSkinPixel = []
    listOfNonSkinPixel = []

    def __init__(self, image, imageMask):
        self.imgMatrix = cv2.imread(image)
        self.width, self.height =  self.imgMatrix.shape[:2]
        self.imageMaskMatrix = cv2.GaussianBlur(cv2.imread(imageMask),(5,5),0)

    """
        Create Image in the Lab color space 
    """
    def convertToLab(self):
        return cv2.cvtColor(self.imgMatrix, cv2.COLOR_BGR2Lab)

    """
        Returns a list of Skin pixels 
    """
    def getSkinPixel(self):
        R, G, B = cv2.split(self.imageMaskMatrix)
        print("Get skin pixel")
        for i in range(self.width):
            print(i)
            for j in range(self.height):
                if R[i][j] == 255 and G[i][j] == 255 and B[i][j] == 255:
                    self.listOfSkinPixel.append({'x':i, 'y':j})


    """
        Returns a list of non Skin pixels 
    """
    def getNonSkinPixel(self, ):
        print("Get non skin pixel")
        R, G, B = cv2.split(self.imageMaskMatrix)
        for i in range(self.width):
            print(i)
            for j in range(self.height):
                if R[i][j] == 0 and G[i][j] == 0 and B[i][j] == 0:
                    self.listOfNonSkinPixel.append({'x': i, 'y': j})


    """
        Get a channel color unique values 
    """
    def getSetABChannelSkinValues(self):
        setOfAChannelSkinValues = []
        Lab = self.convertToLab()
        l, a, b = cv2.split(Lab)
        for pixel in self.listOfSkinPixel:
            print(pixel)
            setOfAChannelSkinValues.append({'a':a[pixel['x']][pixel['y']], 'b':b[pixel['x']][pixel['y']]})
        return setOfAChannelSkinValues

    """
        Skin pixel probabilities 
    
    """
    def getSkinPixelProbabilities(self, a, b):
        count = 0
        for ab in self.getSetABChannelSkinValues():
            if ab['a'] == a and ab['b'] == b :
                count = count + 1
        return count/(self.height*self.width)


