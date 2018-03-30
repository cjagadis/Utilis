import logging as log
import os
import settings

def buildImageList():
    log.info("buildImageList:list of images")
    imgList = os.popen('gcloud compute images list').readlines()
    for text in imgList:
        text = text.split()
        images.append(text[0])
    log.debug(images)
    log.info(("number of images found = ") + str(len(images)))

'''Check the image 
   agains the global list imgLIst
   If the image exist return true
'''
def checkImages(img):
    log.info("in ckeckImages")
    log.debug(img)
    for i in settings.images:
        if i == img:
            log.info("checkImages:image matcheda")
            return True 
    return False
