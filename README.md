# Assignment: Recursion

Create a program that does the following:

1. Recursively finds images in a directory subtree and yields each image found.
2. Creates an empty, RGB image to write thumbnails on (four thumbnails per row).
3. For each source image:
    a. Resize the image to thumbnail size (200 x 200).
    b. Calculate the thumbnail position (row and column).
    c. Pastes the thumnail in the given position.
4. Save the image of thumbnails to a file.

This program contains two files: `foldersearch.py` and `collage.py`.


## `foldersearch.py`

This file is a support library used by the main program (`collage.py`). It contains the following two functions:

### `is_image`: returns whether the given filename is a supported image file, strictly based on the name (extension) of the file.

The function should test each of the `IMAGE_GLOB` patterns to find matches. If any pattern matches, it's an image file. Use the `fnmatch` python module for matching.  Don't use other Python modules, such as glob or re, and don't inspect the file contents.

### `find_images`: the main function of the file.

This is a generator function, which means it acts like a list when called. You may want to read about generators in Python before coding it.

The function uses `os.listdir()` to iterate the file entries of the given directory. Although Python's `os.walk` already does what you need here, you can't use it. You need to code the recursion yourself. As you iterate the entries in a directory, do the following:

* If an entry is an image, it "yields" the image.
* If an entry is a directory, it recursively calls itself using "yield from". The `rootpath` parameter is the same on each call; the `subpath` builds as it gets deeper.

As an example, consider the following directory structure:

```
home/
    pictures/
        pics1/
            picsA
            picsB
                picsH
                    picsK
                picsI
            picsC
        pics2/
            picsM
            picsN
                picsY
                picsZ
            picsO
```

A single call to `find_images('/home/pictures')` essentially does this:

```python
find_images('/home/pictures')
find_images('/home/pictures', 'pics1')
find_images('/home/pictures', 'pics1/picsA')
find_images('/home/pictures', 'pics1/picsB')
find_images('/home/pictures', 'pics1/picsB/picsH')
find_images('/home/pictures', 'pics1/picsB/picsH/picsK')
find_images('/home/pictures', 'pics1/picsB/picsI')
find_images('/home/pictures', 'pics1/picsC')
find_images('/home/pictures', 'pics2')
find_images('/home/pictures', 'pics2/picsM')
find_images('/home/pictures', 'pics2/picsN')
find_images('/home/pictures', 'pics2/picsN/picsY')
find_images('/home/pictures', 'pics2/picsN/picsZ')
find_images('/home/pictures', 'pics2/picsO')
```


## `collage.py`

The assignment template contains a skeleton that will help you get started, including imports, constants, main function, and command-line argument parsing.

When the program starts, it creates an `ArgumentParser` object and parses the arguments. These arguments give 1) the collage file name, and 2) the root directory to search.

Image manipulation is done with the [Python Imaging Library](https://pillow.readthedocs.io/). This is installed with `pip3 install pillow`.  Everything you need is in the `Image` module of PIL.

> Hint: `math.ceil` is a good friend when calculating the number of thumbnail rows needed for the collage.

## Assignment Files



## Submitting the Assignment

When finished, zip your project and submit to the Grader.
