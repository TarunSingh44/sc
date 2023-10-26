import os
import random
import cv2
from captcha.image import ImageCaptcha
import shutil
import numpy as np

lookup = {'#': 0, '%': 1, '+': 2, '-': 3, '0': 4, '1': 5, '2': 6, '3': 7, '4': 8, '5': 9, '6': 10, '7': 11, '8': 12, '9': 13, ':': 14, 'A': 15, 'B': 16, 'D': 17, 'F': 18, 'M': 19, 'P': 20, 'Q': 21, 'R': 22, 'T': 23, 'U': 24, 'V': 25, 'W': 26, 'X': 27, 'Y': 28, 'Z': 29, '[': 30, '\\': 31, ']': 32, 'c': 33, 'e': 34, 'g': 35, 'h': 36, 'j': 37, 'k': 38, 'n': 39, 's': 40}

def generate_captchas(output_dir, symbol, width, height, length, count, fonts):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = ImageCaptcha(width=width, height=height, fonts=fonts)
    for i in range(count):
        random_str = ''.join([random.choice(symbol) for j in range(length)])
        image_path = os.path.join(output_dir, f'{symbol}{i}_{lookup[symbol]}.png')  # Use the content as the filename

        image.write(random_str, image_path)

if __name__ == '__main__':
      # Specify your output directory
    symbols = '#%+-0123456789:ABDFMPQRTUVWXYZ[\]ceghjkns'

    # symbol = "F"  # Customize the character set
    width = 30 # Set your desired image width
    height = 64  # Set your desired image height
    length = 1  # Set the captcha length

    count = 100  # Number of captchas to generate

    fonts = [os.getcwd() + '/The_Jjester.otf']  # Specify the path to your font file
    for symbol in symbols :
       output_dir = os.getcwd() + f'/data_train/train_{symbol}'
       os.makedirs(output_dir, exist_ok = True)
       generate_captchas(output_dir, symbol, width, height, length, count, fonts)
