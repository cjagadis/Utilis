import logging as log
import os
import settings

def buildImageList():
    log.info("buildImageList:list of images")
    imgList = os.popen('gcloud compute images list').readlines()
    for text in imgList:
        text = text.split()
        settings.images.append(text[0])
    log.debug(settings.images)
    log.info(("number of images found = ") + str(len(settings.images)))

