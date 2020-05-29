#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2 as cv
import torch

cv.namedWindow('Cam1')
vc = cv.VideoCapture(0)

if vc.isOpened(): # try to get the first frame.
    r_val, frame = vc.read()

while r_val:
    cv.imshow('Cam1', frame)

    r_val, frame = vc.read()

    x = torch.IntTensor(frame)
    print(x.transponse(axis=1))    # 2D array of image.
    
    key = cv.waitKey(10)
    if key == 27:   # Exit on 'Esc' key.
        break

cv.destroyWindow('Cam1')
