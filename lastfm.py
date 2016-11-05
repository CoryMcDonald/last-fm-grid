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
        album_image = album.item.get_cover_image(pylast.COVER_EXTRA_LARGE)
        file_name = album_image[album_image.rfind('/')+1:]
        if not os.path.isfile(file_name):
            print 'Downloading', file_name
            image_file = urllib.URLopener()
            image_file.retrieve(album_image, file_name)
        file_names.append(file_name)
    
    grid_image = Image.new('RGB', (900,900))

    array_position = 0
    for i in xrange(0,900,300):
        for j in xrange(0,900,300):
            im = Image.open(file_names[array_position])
            grid_image.paste(im, (i,j))
            array_position = array_position + 1
    grid_image.save('ayy.jpg')    
    grid_image.show()

main()

