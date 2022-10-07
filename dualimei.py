from os import name
from re import template
from typing import Sized
import pandas as pd
import code128
from numpy import column_stack, nan
from PIL import Image, ImageFont, ImageDraw 
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep
from os import walk

data = pd.read_excel (r'C:/Users/inci1/Desktop/liste.xlsx',dtype=str,convert_float=1,index_col=None,header=None)

names = data[0].tolist()
names = [item for item in names if not(pd.isnull(item)) == True]

imei1 = data[2].tolist()
imei1 = [item for item in imei1 if not(pd.isnull(item)) == True]
    
imei2 = data[1].tolist()
imei2 = [item for item in imei2 if not(pd.isnull(item)) == True]

for i in range(len(names)):

    barkod1 = code128.image(imei1[i])
    bw, bh = barkod1.size
    barkod1.crop((27, 0, bw-27, bh))

    barkod2 = code128.image(imei2[i])
    bw, bh = barkod2.size
    barkod2.crop((27, 0, bw-27, bh))
    
    template1= Image.open('C:/Users/inci1/Documents/barkcodemaker/dualli.jpg')
    
    tw,th = template1.size

    title_font = ImageFont.truetype('C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 30)
    imei_font = ImageFont.truetype('C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 30)


    template1.paste(barkod1,(480, 250))
    template1.paste(barkod2,(480, 90))

    image_editable = ImageDraw.Draw(template1)

    splitted = names[i].split(" ")
    for j in range(len(splitted)):
        if("GB" in splitted[j]):
            devam=names[i].split(splitted[j])
            devam[1]= (splitted[j]+devam[1])
            #print(devam[0])

    image_editable.text((32,30), devam[0], (0), font=title_font,stroke_width=1,)
    image_editable.text((508,30), devam[1].replace("GB"," GB"), (0), font=title_font,stroke_width=1)
    image_editable.text((508,353), ("IMEI 2:       "+imei1[i]), (0), font=imei_font,stroke_width=1,)
    image_editable.text((508,193), ("IMEI 1:       "+imei2[i]), (0), font=imei_font,stroke_width=1,)

    template1.save("C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_"+str(i)+".pdf")
mergedObject = PdfFileMerger()

for i in range(len(imei1)):
    mergedObject.append(PdfFileReader('C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_' + str(i)+ '.pdf', 'rb'))

mergedObject.write("C:/Users/inci1/Desktop/upload/liste.pdf")


