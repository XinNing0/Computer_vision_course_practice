#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:49:31 2022

@author: xinning
"""
import cv2
import sys,os
import numpy as np


#DIR = '/Users/xinning/Desktop'



if __name__ == "__main__":
    #os.chdir(DIR)
    image_folder = sys.argv[1]
    n = int (sys.argv[2])
    IMAGEs = os.listdir(image_folder)
    Descriptors = []
    print("Nearest Distances")
    
    for index in range(len(IMAGEs)):
        if not IMAGEs[index].endswith('.jpg'):
            continue
        im = cv2.imread(image_folder + '/' + IMAGEs[index])
        Input_size = im.shape
        M, N = Input_size[0], Input_size[1]  ### size of input image
        Sm, Sn = M/n, N/n  ### float value
        downsized_img1 = np.empty((n, n, 3), np.float32)  #  First Downsized Image
        Descriptor = []
        
        for i in range(n):
            for j in range(n):
                block = im[round(i*Sm):round((i+1)*Sm), round(j*Sn):round((j+1)*Sn), 0:3]
                R, G, B = np.mean(block[:,:,0]), np.mean(block[:,:,1]), np.mean(block[:,:,2])
                Descriptor.append(R)
                Descriptor.append(G)
                Descriptor.append(B)
                downsized_img1[i,j,:] = [R, G, B]
                
                
        Descriptor = np.array(Descriptor)
        NORM = np.linalg.norm(Descriptor) / 100
        Descriptors.append(Descriptor/ NORM)
        if index == 0:
            print("First region: %.3f %.3f %.3f" % (downsized_img1[0,0,0], downsized_img1[0,0,1], downsized_img1[0,0,2]))
            print("Last region: %.3f %.3f %.3f" % (downsized_img1[n-1,n-1,0], downsized_img1[n-1,n-1,1], downsized_img1[n-1,n-1,2]))
            
    #for i in range(len(Descriptors)):
    for index in range(len(Descriptors)):
        min_index, MIN = 0, sys.maxsize
        for k in range(len(Descriptors)):
            
            if k == index:
                continue
            tmp_dist = np.linalg.norm(Descriptors[index] - Descriptors[k])
            if tmp_dist < MIN:
                MIN = tmp_dist
                min_index = k
        print("%s to %s: %.2f" % (IMAGEs[index], IMAGEs[min_index], MIN))
