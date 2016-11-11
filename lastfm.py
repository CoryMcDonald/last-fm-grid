from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pylast
import urllib
import os.path

API_KEY = '71cccbdefd11231bc24e3f95d460b2a3'

    

def main():
    user = 'corymcdonald'
    time_period = 'Top Albums (Last 7 Days)'

    network = pylast.LastFMNetwork(api_key = API_KEY)
    albums = network.get_user('corymcdonald').get_top_albums(period=pylast.PERIOD_7DAYS, limit=9)
    file_names = []

    for album in albums:
        album_image = album.item.get_cover_image(pylast.COVER_EXTRA_LARGE)
        file_name = 'images/'
        file_name += album_image[album_image.rfind('/')+1:]
        if not os.path.isfile(file_name):
            print 'Downloading', file_name
            image_file = urllib.URLopener()
            image_file.retrieve(album_image, file_name)
        file_names.append([file_name, album.item.artist.name, album.item.title])

    grid_image = Image.new('RGB', (900,950))
    font = ImageFont.truetype("Roboto-Medium.ttf", 32)
    small_font = ImageFont.truetype("SourceCodePro-Medium.ttf", 16)
    draw = ImageDraw.Draw(grid_image, 'RGBA')

    array_position = 0
    for i in xrange(0,900,300):
        for j in xrange(50,900,300):
            artist_name = file_names[array_position][1]
            album_title = file_names[array_position][2]
            album_title = (album_title[:27] + '..') if len(album_title) > 27 else album_title
            artist_name = (artist_name[:27] + '..') if len(artist_name) > 27 else artist_name

            im = Image.open(file_names[array_position][0])
            grid_image.paste(im, (i,j))
            # lmao making an outline for the text is dumb
            draw.text((i+2, j+2), artist_name,(0,0,0),font=small_font)
            draw.text((i+1, j+1), artist_name,(255,255,255),font=small_font)

            draw.text((i+2, j+21), album_title,(0,0,0),font=small_font)
            draw.text((i+1, j+20), album_title,(255,255,255),font=small_font)

            array_position = array_position + 1

    draw.text((10, 5), user + ' - ' + time_period ,(255,255,255),font=font)
    grid_image.save('lol.png')


main()

