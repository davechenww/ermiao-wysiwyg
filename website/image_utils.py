# -*- coding:utf-8 -*-
import uuid
import os
import settings
    
def save(uploadfile):
    random_name = '%s.png' % uuid.uuid4().hex

    uri = os.path.join(settings.MEDIA_ROOT, 'uploads', random_name)
    dest = open(uri, 'wb+')
    for chunk in uploadfile.chunks():
        dest.write(chunk)
    dest.close()

    url = os.path.join(settings.MEDIA_URL, 'uploads', random_name)
    return url 
        
