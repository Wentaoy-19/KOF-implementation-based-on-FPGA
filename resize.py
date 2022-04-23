# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 23:34:11 2021

@author: Lenovo
"""

#from PIL import Image
#filename = input("What's the image prefix name? ")
#new_w, new_h = map(int, input("What's the new height x width? Like 28 28. ").split(' '))
#frame = int(input("What's the frame number? "))
#folder = input("What's the folder name? ")
#for j in range(frame):
#    if j < 10:
#        number = "0" + str(j)
#    else:
#        number = str(j)
#    number = str(j)  

#    img = Image.open("./sprite_originals/KOF/Iori2/" + folder +"/" + filename + number + ".png")
#    out = img.resize((new_w, new_h))
#    out.save("./sprite_originals/KOF/Iori3/" + folder +"/" + filename + number + ".png")


from PIL import Image
img = Image.open("./sprite_originals/KOF/component/KO.png")
out = img.resize((71,63))
out.save("./sprite_originals/KOF/component/KO_resize2.png")