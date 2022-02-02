#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:21:53 2022

@author: xinning
"""



import cv2
import sys,os
import numpy as np


if __name__ == "__main__":
    
    im = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)  ### type is np.ndarray
    #print(im.shape)  # (375, 270)
    Input_size = im.shape
    M, N = Input_size[0], Input_size[1]  ### size of input image
    m, n = int(sys.argv[2]), int(sys.argv[3])  ### size of 1st downsized image
    Sm, Sn = M/m, N/n  ### float value
    b = int (sys.argv[4])
    
    ##########################  First Downsized Image  #######################
    downsized_img1 = np.empty((m, n), np.float32)  #  First Downsized Image
    
    for i in range(m):
        for j in range(n):
            block = im[round(i*Sm):round((i+1)*Sm), round(j*Sn):round((j+1)*Sn)]
            aver_intensity = np.mean(block)
            downsized_img1[i,j] = aver_intensity
    ##########################  First Downsized Image  #######################

    #########################  Secondt Downsized Image  #######################
    MEDIAN = np.median(downsized_img1)
    lambda_median = lambda a : True if (a >= MEDIAN) else False
    downsized_img2 = np.empty((m, n), np.float32)  #  Second Downsized Image
    for i in range(m):
        for j in range(n):
            val = 255 if lambda_median(downsized_img1[i, j]) else 0
            downsized_img2[i, j] = val
    #########################  Second Downsized Image  #######################
    
    res_image1 = np.empty((m * b, n * b), np.float32)
    res_image2 = np.empty((m * b, n * b), np.float32)
    for i in range(m):
        for j in range(n):
            
            res_image1[i*b : (i+1)*b, j*b : (j+1)*b] = downsized_img1[i,j]
            res_image2[i*b : (i+1)*b, j*b : (j+1)*b] = downsized_img2[i,j]
    ######################## Save two images #################################
    
    downsized_img1_round = np.round_(res_image1)
    input_image_name = sys.argv[1].split('.')
    output1_name = input_image_name[0] + '_g.' + input_image_name[1]
    output2_name = input_image_name[0] + '_b.' + input_image_name[1]
    cv2.imwrite(output1_name, downsized_img1_round.astype(np.uint8))
    print("Downsized images are (%d, %d)" % (m, n))
    
    
    #downsized_img2_block = np.tile(downsized_img2, (b, b))
    cv2.imwrite(output2_name, res_image2.astype(np.uint8))
    print("Block images are (%d, %d)" % (m * b, n * b))
    ######################## Save two images #################################
    
    
    ######################## Check intensities ################################
    loc1, loc2, loc3, loc4 = [m//4, n//4], [m//4, 3* n//4], [3* m//4, n//4], [3* m//4, 3* n//4]
    print("Average intensity at (%d, %d) is %f" % (loc1[0], loc1[1], round(downsized_img1[loc1[0], loc1[1]])))
    print("Average intensity at (%d, %d) is %f" % (loc2[0], loc2[1], round(downsized_img1[loc2[0], loc2[1]])))
    print("Average intensity at (%d, %d) is %f" % (loc3[0], loc3[1], round(downsized_img1[loc3[0], loc3[1]])))
    print("Average intensity at (%d, %d) is %f" % (loc4[0], loc4[1], round(downsized_img1[loc4[0], loc4[1]])))
    ######################## Check intensities ################################
    
    
    print("Binary threshold: %s" % MEDIAN)
    print("Wrote image %s" % output1_name)
    print("Wrote image %s" % output2_name)