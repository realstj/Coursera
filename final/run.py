#! /usr/bin/env python3

import os
import requests

fruits = {}
keys = ["name", "weight", "description", "image_name"]
index = 0
path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"
url = "http://34.145.71.130/fruits/"

files = os.listdir(path)
img_files = os.listdir(img_path)

for file in files:
    with open(path + file) as f:
        for ln in f:
            line = ln.strip()
            if "lbs" in line:
                nline = line.split()
                wght = int(nline[0])
                fruits["weight"] = wght
                index += 1
            else:
                try:
                    fruits[keys[index]] = line
                    index += 1
                except:
                    fruits[keys[2]] = line
        index = 0
        split_f = file.split(".")
        name = split_f[0] + ".jpeg"
        for fle in img_files:
            if fle == name:
                fruits["image_name"] = name
        response = requests.post(url, json=fruits)
        fruits.clear()