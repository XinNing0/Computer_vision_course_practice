#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:43:28 2022

@author: xinning
"""

import cv2
import sys
import numpy as np

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])



if __name__ == "__main__":
    '''
    Now onto the real stuff.  First, check the command line arguments.
    '''
    #if len(sys.argv) != 3:
    #   print('Incorrect number of arguments!')
    #    sys.exit()

    '''
    Open and read the image.
    '''
    im = cv2.imread(sys.argv[1])
    # (1080, 1920, 3)
    SHAPE = im.shape
    diff = int((SHAPE[1] - SHAPE[0]) / 2)
    l1, l2, r1, r2 = 0, diff, SHAPE[0] - 1, SHAPE[0] + diff -1
    
    cropped_image = im[l1:l2, r1:r2]
    M = int(sys.argv[3])
    N = int(sys.argv[4])
    down_points = (M, M)
    resized_image = cv2.resize(cropped_image, down_points)
    flipped_image = cv2.flip(resized_image, 0)
    
    downsized_revered_image = 255 - resized_image
    upsideDown_revered_image = 255 - flipped_image
    
    grid_image = concat_tile([[resized_image, downsized_revered_image],
                       [upsideDown_revered_image, flipped_image]])
    final_image = np.tile(grid_image, (N, N, 1))
    
    #Image mountain3.jpg cropped at (0, 420) and (1079, 1499)
    cv2.imwrite(sys.argv[2], final_image)
    print ("Image %s cropped at (%d, %d) and (%d, %d)" % (sys.argv[1], l1, l2, r1, r2) )
    print ("Resized from (%d, %d, 3) to (%d, %d, 3)" % (SHAPE[0], SHAPE[0], M, M))
    print("The checkerboard with dimensions %d X %d was output to %s" % (2*M*N, 2*M*N, sys.argv[2]))

    #while(1):
    #    cv2.imshow('hanhan',final_image)
    #    if cv2.waitKey(1)&0xFF == ord('q'):
    #        cv2.destroyAllWindows()
    #        brea 
    
    #if im is None:
    #    print("Failed to open image", sys.argv[1])
    #    sys.exit()
    
    
      
