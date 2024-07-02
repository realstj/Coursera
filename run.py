#! /usr/bin/env python3

import os
import requests

path = "/data/feedback/"
keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)

for file in folder:
      count = 0
      fb = {}
      with open(path + file) as feed_list:
            for line in feed_list:
                  value = line.strip()
                  fb[keys[count]] = value
                  count += 1
      print(fb)
      response = requests.post("http://34.105.64.234/feedback", json=fb)
print(response.request.body)
print(response.status_code)