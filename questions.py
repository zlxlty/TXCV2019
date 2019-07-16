'''
@Description: Qualifying Exam for TXCV
@Author: Tianyi Lu
@Date: 2019-07-16 12:23:31
@LastEditors: Tianyi Lu
@LastEditTime: 2019-07-16 14:15:14
'''
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import matplotlib.pyplot as plt
# PIL use RGB while OpenCV use BGR
DEFAULT_DIR = 'pic'

def question1(target_dir):
    '''
    @description: create a "HELLO WORLD" image
    @param {target_dir: the dir to save pictures}
    @return: None
    @save: 'hello.png' PNG picture
    '''
    background = Image.new('RGB', (130, 35), (255,255,255))
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 15)

    d = ImageDraw.Draw(background)
    d.text((10, 10), "HELLO WORLD", font=fnt, fill=(0, 0, 0))

    background.save(''.join([target_dir,'/','Q1_answer.png']))


def question2_PIL(target_dir):
    '''
    @description: Use Pillow module to enhance the alpha channel
    @param {target_dir: the dir to save pictures} 
    @return: PIL.Image.Image
    @save: 'Q2_answer_PIL.png' PNG picture
    '''
    im = Image.open('Q2.png').convert('RGBA')

    R, G, B, A = im.split()
    A = A.point(lambda i: i+255)

    im = Image.merge('RGBA', (R, G, B, A))

    im.save(''.join([target_dir,'/','Q2_answer_PIL.png']))
    
    return im


def question2_CV(target_dir):
    '''
    @description: Use OpenCV module to enhance the alpha channel
    @param {target_dir: the dir to save pictures} 
    @return: numpy.ndarray
    @save: 'Q2_answer_CV.png' PNG picture
    '''
    im = Image.open('Q2.png').convert('RGBA')
    img = np.array(im)
    img[:,:,3] += 255
    
    cv2.imwrite(''.join([target_dir,'/','Q2_answer_CV.png']), img)    

    return img

def question3(target_dir):
    '''
    @description: change the alpha channel for black pixels to zero
    @param {target_dir: the dir to save pictures} 
    @return: numpy.ndarray
    @save: 'Q3_answer.png' PNG picture
    '''
    img = question2_CV(target_dir)
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            if np.sum(img[r, c, 0:3]) == 0:
                img[r, c, 3] = 0

    cv2.imwrite(''.join([target_dir,'/','Q3_answer.png']), img)

    return img

def question4(target_dir):
    '''
    @description: enlarge picture in question3 by two and copy a new one to the right
    @param {target_dir: the dir to save pictures} 
    @return: None
    '''
    img = question3(target_dir)
    img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2)) # order in resize is (width, height)
    img = np.concatenate((img, img), axis=1)
    cv2.imwrite(''.join([target_dir,'/','Q4_answer.png']), img)

def run_exam(target_dir):
    '''
    @description: answer all the questions
    @param {target_dir: the dir to save pictures} 
    @return: None
    '''
    question1(target_dir)
    question2_PIL(target_dir)
    question4(target_dir)

if __name__ == '__main__':

    try:
        target_dir = sys.argv[1]
    except IndexError:
        target_dir = DEFAULT_DIR
    if target_dir not in os.listdir():
        os.mkdir(target_dir)
    
    run_exam(target_dir)