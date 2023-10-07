# coding: UTF-8
from apriltag import apriltag
import cv2
import numpy as np
import sys

img =cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detector = apriltag("tag36h11")
tags = detector.detect(gray)
longs = len(tags)

if longs > 0 :
    print("%d apriltags have been detected."%len(tags))
    print(tags)
    arr = np.array(tags[0]["lb-rb-rt-lt"],np.int).reshape(1,4,2)
    Img = cv2.polylines(img,arr,True,(0,0,255),2)
    Img = cv2.circle(img,tuple(map(int,tags[0]["center"])), 4, (2,180,200), 2)
    cv2.imwrite("apriltag_test.jpg",Img)
else:
    print("%d apriltags have been detected."%len(tags))

'''
# 进行apriltag检测，得到检测到的apriltag的列表
print("%d apriltags have been detected."%len(tags))
print(tags)
arr = np.array(tags[0]["lb-rb-rt-lt"],np.int).reshape(1,4,2)
Img = cv2.polylines(img,arr,True,(0,0,255),2)
Img = cv2.circle(img,tuple(map(int,tags[0]["center"])), 4, (2,180,200), 2)
'''

'''
lens = len(tags) - 1
num = range[0, lens]
print(num)
# print(tags[0]["lb-rb-rt-lt"][0])

for i in num:
        cv2.circle(img, tuple(tag[i]["lb-rb-rt-lt"][3], 4,(255,0,0), 2) # left-top
        cv2.circle(img, tuple(tag[i]["lb-rb-rt-lt"][2], 4,(255,0,0), 2) # right-top
        cv2.circle(img, tuple(tag[i]["lb-rb-rt-lt"][1], 4,(255,0,0), 2) # right-bottom
        cv2.circle(img, tuple(tag[i]["lb-rb-rt-lt"][0], 4,(255,0,0), 2) # left-bottom
'''
# cv2.imwrite("apriltag_test.jpg",Img)
