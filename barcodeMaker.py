from os import name
from re import template
from typing import Sized
import pandas as pd
import code128
from numpy import column_stack, nan
from PIL import Image, ImageFont, ImageDraw 
from PyPDF2 import PdfFileMerger, PdfFileReader

from time import sleep

data = pd.read_excel (r'C:/Users/inci1/Desktop/liste.xlsx',dtype=str,convert_float=1,index_col=None,header=None)

imei = data[0].tolist()
imei = [item for item in imei if not(pd.isnull(item)) == True]

names = data[1].tolist()
names = [item for item in names if not(pd.isnull(item)) == True]

for i in range(len(imei)):


    barkod = code128.image(imei[i])
    bw, bh = barkod.size
    barkod.crop((27, 0, bw-27, bh))
    barkod=barkod.resize([int(bw/1.05),bh-17])

    barkod2 = code128.image(names[i])
    bw2, bh2 = barkod2.size
    barkod2.crop((27, 0, bw2-27, bh2))
    barkod2=barkod2.resize([int(bw2/1.05),bh2-17])

    template1= Image.open('C:/Users/inci1/Desktop/template.jpg')
    
    tw,th = template1.size

    imei_font = ImageFont.truetype('C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 40)

    template1.paste(barkod,(20, 295))
    template1.paste(barkod2,(20, 440))

    image_editable = ImageDraw.Draw(template1)

    print(imei[i])
    print(names[i])
    

    image_editable.text((50,380), (imei[i]), (0,0,0), font=imei_font,stroke_width=1,)
    image_editable.text((50,530), (names[i]), (0,0,0), font=imei_font,stroke_width=1,)

    template1.save("C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_"+str(i)+".pdf")


mergedObject = PdfFileMerger()

for i in range(len(imei)):
    mergedObject.append(PdfFileReader('C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_' + str(i)+ '.pdf', 'rb'))
 
mergedObject.write("C:/Users/inci1/Desktop/upload/liste.pdf")