# -*- coding:utf-8 -*-

import re

def get_image(str):
    image_pattern = re.compile(ur'<img.*">') 
    return re.findall(image_pattern, str)
