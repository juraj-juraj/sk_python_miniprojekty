# Program spája funkcionalitu ostatných dvoch programov 
# Pri spustení by sa mal otvoriť dialógové okno, ktoré sa pýta na obrázok, ktorý chceme otvoriť
# Boli problémy, pretože nie každému fungovalo to dialógové okno a všeobecne prevody obrázkov sa ukázali byť ťažšie na pochopenie ako som myslel

import tkinter
from tkinter import filedialog
from pixel_art import convert_to_char, print_2Dlist
from bw_convert import convert_bw

tkinter.Tk().withdraw()

action = input("Would you like to convert to black'n white(bw) or chracters(chr): ")

image_path = filedialog.askopenfilename()

if(action == "chr"):
    photo_list = convert_to_char(image_path)
    print_2Dlist(photo_list)

elif(action == "bw"):
    convert_bw(image_path, "updated_greyscale.jpg", technology="greyscale")
    convert_bw(image_path, "updated_treshold.jpg", technology="treshold")
    convert_bw(image_path, "updated_rand_treshold.jpg", technology="rand_treshold")
