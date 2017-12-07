from __future__ import print_function
import flickr_api
from flickr_api import Photo
import sys
import os

lat = -34.6076094
lon = -58.4456606

path_out = '/home/xxx/Documents/images/'
flickr_api.set_keys(api_key = 'xxxxxxxxxxxxxxxxxxxxx', api_secret = 'xxxxxxxxxxxxx')

# step1: Creating directory 
if not os.path.exists(path_out):
    print("Creating directory " + path_out)
    os.mkdir(path_out)
os.chdir(path_out)

# step2: traverse each page to get the images
for i in range(1,10):
    photo_list = Photo.search(tags="buildings", lat=lat, lon=lon, radius=5.0, per_page=250, page=i)
    #photo_list = Photo.photosForLocation(lat=lat, lon=lon, accuracy=11, per_page=500, page=i)
    print("images on current page: "+str(len(photo_list)))

    for photo in photo_list:
        try:
            loc = photo.getLocation()
            name = str(loc.latitude)+","+str(loc.longitude)
            print("Saving photo "+name)
            photo.save(path_out+name+".jpg", 'Large')
        except Exception as e:
            print('failed to download image')






