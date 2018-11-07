# SKIN DETECTION SOFTWARE
This Skin detection software is to detect people skin from images. 
For this purpose we will use a data set of images and their ground (mask)
## Cleaning data 
To adapt the data set to our softwere, each image and it ground 
image should have the same name and put in the respecitive folder
:
- data/set : for original images
- data/skin_mask : ground skin images 
- data/non_skin_mask : non skin ground images.  
**NB:** _We are not going to use non ground skin images, but 
rather detect non ground skin pixel from ground images_

# Skin Histogram
## 1st we have to match skin pixels:
From the skin mask and the orignal image we can match all skin pixel 
1. Get All skin pixel position
2. Use this positions to get the skin pixel values from the original image 
3. Calculate the two dimension histogram of the skin pixels values

NB: The two dimension histogram is the probability of appearence of the a and b channel in an image

# Not Skin Histogram
## 2nd from the non skin mask and the original image we can match all not skin pixels 
1. Get all non position 
2. use this positions to get the non skin pixel value from the original image 
3. Calculate the two dimension histogram of the non skin pixels values

# Evaluate / Test 
For each pixel from the test image, get it a and b channel and check it value from each histogram
( skin histogram and non skin histogram). 
The heighest value determines whether the given pixel is a skin or a non skin.
    
# Tools 
To acheive this work we installed in our virtual environment the 
following tools:
- pip install numpy
- pip install opencv-python
