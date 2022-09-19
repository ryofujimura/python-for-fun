'''
shoheihomegorund

This script is to add watermark to images.
run through all files in the directory and add watermark to them.

'''

import os
import sys
import glob
from PIL import Image, ImageDraw, ImageFont

# # giving directory name
dirname = '/Volumes/OREnoPIC/LAA/shoheihomeground/wallpaper'
# newdir = '/nofilefound/Volumes/OREnoPIC/2015-2018/deletedfiles/'
# # giving file extension

ext = ('m4v', 'jpg','mp4')
# # iterating over all files
contain = ")"
list = []

for file in glob.glob(dirname+"*"):
    for newfile in glob.glob(file+"/*"):
        list.append(newfile)
        for newnewfile in glob.glob(newfile+"/*"):
            list.append(newnewfile)
            for newnewnewfile in glob.glob(newnewfile+"/*"):
                list.append(newnewnewfile)
                # for newnewnewnewfile in glob.glob(newnewnewfile+"/*"):
                #     list.append(newnewnewnewfile)

print(list)
# for files in list:
#     # print(files)
#     if contain in files:
#         # printing file name of desired extension
#         print(files)
#         # os.remove(files)
#     else:
#         continue
