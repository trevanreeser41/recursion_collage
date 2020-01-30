#!/usr/bin/env python3
import argparse
import os
import math
from PIL import Image               # pip3 install pillow
from foldersearch import find_images

THUMBNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200

########################
###  Main program

def main(args):
    '''
    Creates a collage by recursively finding images in a directory path.
    '''
    # find the images
    imgpaths = []
    for filepath in find_images(args.searchpath):
        imgpaths.append(filepath)
    if len(imgpaths) == 0:
        print('No images found')
        return

    print(imgpaths)

    # # create a new, RGB image
    num_rows = math.ceil(len(imgpaths)/THUMBNAILS_PER_ROW)
    collage = Image.new("RGB", (THUMBNAILS_PER_ROW*THUMBNAIL_WIDTH, num_rows*THUMBNAIL_HEIGHT))

    # place the thumbnails
    current_col = 0
    current_row = 0
    for imgnum, imgpath in enumerate(imgpaths):
        print(f'=> {imgpath}')
        # open the image and convert to RGB
        im = Image.open(imgpath)
        im.convert("RGB")
        # resize to a thumnail
        im.thumbnail((THUMBNAIL_HEIGHT, THUMBNAIL_WIDTH))
        # paste in next position
        collage.paste(im, (current_col * THUMBNAIL_WIDTH, current_row * THUMBNAIL_HEIGHT))
        current_col += 1
        if current_col >= THUMBNAILS_PER_ROW:
            current_row += 1
            current_col = 0

    # save the image
    collage.save(args.collage)
    print(f'Writing {args.collage}')

########################
###  Bootstrap

parser = argparse.ArgumentParser(description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
