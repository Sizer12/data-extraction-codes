from csv import writer
from os import device_encoding, name
from random import randrange
from re import template
import pandas as pd
import code128
from numpy import column_stack, nan
from PIL import Image, ImageFont, ImageDraw
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep
import random

#########################

device = "HAYLOU T15"
forname = 'T15/'
imei = [random.randint(10**(15-len(forname)-1), 10**(15-len(forname))-1)]
#imei = [10000001155]
adet = 540
deviceNameAlligment = 150

#########################

for j in range(adet-1):
    imei.append(imei[j]+1)
for m in range(len(imei)):
    imei[m] = forname+str(imei[m])

df = pd.DataFrame(imei)
writer = pd.ExcelWriter("C:/Users/inci1/Desktop/upload/" +
                        device+".xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()

for i in range(len(imei)):

    barkod = code128.image(imei[i])
    bw, bh = barkod.size
    #barkod=barkod.crop((27, 0, bw-27, bh))
    barkod = barkod.resize([495, bh])
    template1 = Image.open('C:/Users/inci1/Desktop/blank.png')

    tw, th = template1.size

    imei_font = ImageFont.truetype(
        'C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 35)

    device_font = ImageFont.truetype(
            'C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 25)

    template1.paste(barkod, (0, 60))
    template1.paste(barkod, (0, 90))

    image_editable = ImageDraw.Draw(template1)

    image_editable.text(
        (105, 200), (imei[i]), (0), font=imei_font, stroke_width=1,)
    image_editable.text((deviceNameAlligment, 5), (device),
                        (0), font=imei_font, stroke_width=1,)

    template1.save(
        "C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_"+str(i)+".pdf")

mergedObject = PdfFileMerger()

for i in range(len(imei)):
    mergedObject.append(PdfFileReader(
        'C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_' + str(i) + '.pdf', 'rb'))

mergedObject.write("C:/Users/inci1/Desktop/upload/"+device+".pdf")
