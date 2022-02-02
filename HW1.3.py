#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:07:32 2022

@author: xinning
"""

import cv2
import sys
import numpy as np
from PIL import Image
from itertools import product
from numpy import array
np.printoptions(precision = 3)
    
if __name__ == "__main__":
    '''
    Now onto the real stuff.  First, check the command line arguments.
    '''
    #if len(sys.argv) != 3:
    #    print('Incorrect number of arguments!')
    #    sys.exit()

    '''
    Open and read the image.
    '''

    
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    dir = sys.argv[3]
    
    im = cv2.imread(input_name)
    (M, N) = im.shape[:2]
    
    if dir == 'right' or dir == 'left':
        multi = np.arange(0, N) / (N - 1)
        multi = np.flip(multi)
        multi = np.tile(multi, (M, 1))

    elif dir == 'top' or dir == 'bottom':
        multi = np.arange(0, M) / (M - 1)
        multi = np.flip(multi)
        multi = multi.reshape(-1, 1)
        multi = np.tile(multi, (1, N))
    
    elif dir == 'center':
        multi = np.arange(M //2 ) /(N //2)
        multi = np.flip(multi)
        multi = multi.reshape(1, -1)
        multi = np.tile(multi, (M, N))
        
        
        
    
    print('({},{}) {:.3f}'.format(0, 0, multi[0][0]))
    print('({},{}) {:.3f}'.format(0, N//2, multi[0][N//2]))
    print('({},{}) {:.3f}'.format(0, N-1, multi[0][N-1]))
    print('({},{}) {:.3f}'.format(M//2, 0, multi[M//2][0]))
    print('({},{}) {:.3f}'.format(M//2, N//2, multi[M//2][N//2]))
    print('({},{}) {:.3f}'.format(M//2, N-1, multi[M//2][N-1]))
    print('({},{}) {:.3f}'.format(M-1, 0, multi[M-1][0]))
    print('({},{}) {:.3f}'.format(M-1, N//2, multi[M-1][N//2]))
    print('({},{}) {:.3f}'.format(M-1, N-1, multi[M-1][N-1]))
    

    
    #print(len(im[0]))
    #(1920, 1080, 3)
    
    #r,g,b, alpha_channel = im.split()

    #alpha = im.astype(float)/255

    
    mask1 = np.repeat(np.tile(np.linspace(1, 0, im.shape[1]), (im.shape[0], 1))[:, :, np.newaxis], 3, axis=2)
    right = np.uint8(im * mask1 )
    right_image =  np.concatenate((im, right), axis=1)
    
    mask2 = np.repeat(np.tile(np.linspace(0, 1, im.shape[1]), (im.shape[0], 1))[:, :, np.newaxis], 3, axis=2)
    center = np.uint8(right * mask2 )
    center_image = np.concatenate((im, center), axis=1)
    
    mask3 = np.repeat(np.tile(np.linspace(1, 0, im.shape[0]), (im.shape[1], 1))[:, :, np.newaxis], 3, axis=2)
    mask4 = cv2.rotate(mask3, cv2.cv2.ROTATE_90_CLOCKWISE)
    bottom = np.uint8(im * mask4 )
    bottom_image = np.concatenate((im, bottom), axis=1)
    
    if dir == 'right' or dir == 'left':
        cv2.imwrite(output_name, right_image)

    elif dir == 'top' or dir == 'bottom':
        cv2.imwrite(output_name, bottom_image)
    
    elif dir == 'center':
        cv2.imwrite(output_name, center_image)
    
    
     
#     SHAPE=bottom.shape
#         
#     M=SHAPE[1]  
#     N=SHAPE[0]
#     
#     list_a = (0, M/2, M-1)
#     list_b = (0, N/2, N-1)
#     
#     res = list(product(list_a, list_b))
#         
#     print(SHAPE)
# =============================================================================
 


    
    
    #if im is None:
    #    print("Failed to open image", sys.argv[1])
    #    sys.exit()
    

  

    #while(1):  
    #     cv2.imshow('hello', right_image)
    #     if cv2.waitKey(1)&0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break 
