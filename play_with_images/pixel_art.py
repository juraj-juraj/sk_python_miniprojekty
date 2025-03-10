# Tento program prerobí zadaný obrázok na ascii art
# Deti samozrejme dostali kostru, do ktorej len dopĺňali

from PIL import Image

gray_pixels = ['#', '%', '1', '!','+', ':','.',' ']

def convert(input, in_high = 255, out_high = len(gray_pixels)-1):
    return round((input / in_high) * out_high)

def count_intensity(red, green, blue):
    # Vzorec je založený na fyziológii ľudského oka a ako vníma rôzne farby
    return round(0.299 * red + 0.587 * green + 0.114 * blue)

def init_2D_list(width, height):
    return [[0]*width for i in range(height)]

# out_width a height je veľkosť výstupného obrázku v riadkoch a znakoch na šírku
def convert_to_char(image_name, out_width = 156, out_height = 64):
    photo = Image.open(image_name, 'r')
    photo_resized = photo.resize((out_width, out_height))
    photo_list = init_2D_list(out_width, out_height)

    width, height = photo_resized.size
    for y in range(height):
        for x in range(width):
            pixel_val = photo_resized.getpixel((x,y))
            intensity = count_intensity(pixel_val[0], pixel_val[1], pixel_val[2])
            # intensity je v rozsahu <0, 255> a treba to prepočitať do rozsahu <0, len(gray_pixels)>
            index = convert(intensity)
            photo_list[y][x] = gray_pixels[index]

    return photo_list

def print_2Dlist(photo_list):
    height = len(photo_list)
    width = len(photo_list[0])
    for y in range(height):
        for x in range(width):
            print(photo_list[y][x], end='')
        print('')

if(__name__ == "__main__"):
    image_name = input("Write Image name: ")
    photo_list = convert_to_char(image_name)
    print_2Dlist(photo_list)
