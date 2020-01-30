#!/usr/bin/env python3
import os
import fnmatch

images = []
rootpath = 'C:/Users/trevanreeser41/Desktop/Winter_MISM/537/recursion/recursion/pictures'

IMAGE_GLOBS = {
    '*.png',
    '*.jpg',
   '*.jpeg',
}

def is_image(filename):
    '''
    Returns True if the given filename matches one of the IMAGE_GLOBS patterns.
    Just check the filename itself (don't inspect the file contents).
    '''
    for suffix in IMAGE_GLOBS:
        if fnmatch.fnmatch(filename, suffix):
            return True
        else:
            False
    pass   # placeholder here so the file will compile

def find_images(rootpath, subpath=''):
    '''
    Generator function that returns the images in the given directory
    tree (includes subdirectories). The returned image paths are relative to
    the given path.

    Use os.listdir() to get the files in the current directory (don't use os.walk
    or glob.glob).
    '''
    dir = os.listdir(os.path.abspath(rootpath + subpath))
    for path in dir:
        full_path = os.path.join(rootpath,path)
        if os.path.isdir(full_path):
            for entry in find_images(full_path):
                yield entry
        elif os.path.isfile(full_path):
            if is_image(full_path):
                yield full_path
        
        else:
            print('Unable to find photos')

    pass    # placeholder here so the file will compile