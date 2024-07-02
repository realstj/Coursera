### This python code imports Image function from the PIL package
### Code below will turn the image 90 degrees clockwise
### Then converts tiff images with size of 192 x 192 pixels into
### jpeg formate with 128 x 128 size. 
### At the end, converted images will be stored in the folder: /apt/icons/

#!/usr/bin/env python3

import os
from PIL import Image

# set source and target dirs:
# NOTE: lab calls for new images to be stored to system root
src_dir = "images/"
new_dir = "/opt/icons/"

# set reprocess vars:
rot_deg = -90
re_size = (128, 128)

new_format = "JPEG"

# gather list of image files:
img_files = [f for f in os.listdir(src_dir) if f.startswith("ic_")]

# reprocess images:
for file in img_files:
    src_img = Image.open(src_dir + file)

    # rotate & resize image:
    new_img = src_img.rotate(rot_deg).resize(re_size)

    # NOTE: we need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")

    # save new output file:
    new_img.save(new_dir + file, new_format)