from PIL import Image
import pylast
import urllib
import os.path

API_KEY = '71cccbdefd11231bc24e3f95d460b2a3'

def main():
    network = pylast.LastFMNetwork(api_key = API_KEY)
    albums = network.get_user('corymcdonald').get_top_albums(period=pylast.PERIOD_7DAYS, limit=9)
    file_names = []

    for album in albums:
        album_image = album.item.get_cover_image(pylast.COVER_MEDIUM)
        file_name = album_image[album_image.rfind('/')+1:]
        if not os.path.isfile(file_name):
            print 'Downloading', file_name
            image_file = urllib.URLopener()
            image_file.retrieve(album_image, file_name)
        file_names.append(file_name)
    
        

main()
