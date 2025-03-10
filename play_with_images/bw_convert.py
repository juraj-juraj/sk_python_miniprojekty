# Program na prevod obrázkov na čiernobielo alebo odtiene šedej
# Deti to veľmi nebavilo, bolo to náročné na pochopenie a taktiež boli problémy s inštalovaním knižníc

from PIL import Image
from random import randrange

MAX_PIXEL_VAL = 255
MIN_PIXEL_VAL = 0

def count_intensity(red, green, blue):
    return round(0.299 * red + 0.587 * green + 0.114 * blue)

def greyscale_tech(pixel):
    intensity = count_intensity(pixel[0], pixel[1], pixel[2])
    return (intensity, intensity, intensity)

# V oboch prahovacích technológiách sa najprv vypočíta šedotónový odtieň a potom sa porovná s prahom
def treshold_tech(pixel, treshold = 125):
    mod_pixel = greyscale_tech(pixel)
    if(mod_pixel[0] > treshold):
        return (MAX_PIXEL_VAL, MAX_PIXEL_VAL, MAX_PIXEL_VAL)
    else:
        return (MIN_PIXEL_VAL, MIN_PIXEL_VAL, MIN_PIXEL_VAL)

def rand_treshold_tech(pixel):
    mod_pixel = greyscale_tech(pixel)
    treshold = randrange(MIN_PIXEL_VAL+1, MAX_PIXEL_VAL-1)
    if(mod_pixel[0] > treshold):
        return (MAX_PIXEL_VAL, MAX_PIXEL_VAL, MAX_PIXEL_VAL)
    else:
        return (MIN_PIXEL_VAL, MIN_PIXEL_VAL, MIN_PIXEL_VAL)


def convert_bw(photo_name, mod_photo_name = "updated.jpg", technology = "greyscale"):
    photo = Image.open(photo_name, 'r')
    width, height = photo.size
    mod_photo = Image.new("RGB", photo.size)

    # Obrázkom sa prejde ako dvojrozmerným poľom a pre každý jeden pixel sa vypočíta farba
    # Podľa zadanej technológie sa pre každý pixel počíta intenzita
    for y in range(height):
        for x in range(width):
            # Po jednom pixeli sa chodí, vypočita sa jeho farba a zapíše sa do obrázku
            pixel_val = photo.getpixel((x,y))
            if(technology == "greyscale"):
                mod_pixel = greyscale_tech(pixel_val)
            elif(technology == "treshold"):
                mod_pixel = treshold_tech(pixel_val)
            elif(technology == "rand_treshold"):
                mod_pixel = rand_treshold_tech(pixel_val)
            mod_photo.putpixel((x,y), mod_pixel)
    
    mod_photo.save(mod_photo_name, "JPEG")

if (__name__ == "__main__"):
    nazov_obrazku = input("Zadaj cestu k obrazku: ")
    # prepina sa medzi technologiami prerobenia na čierno-biely obraz a medzi prevodom do šedotónového
    # technologie: greyscale - prevod do šedotónových farieb
    #              treshold_tech - prevod na čierno-biely prahovaním
    #              rand_treshold_tech - prevod na čierno-biely náhodným prahovaním

    convert_bw(nazov_obrazku, "updated.jpg", technology="rand_treshold")

