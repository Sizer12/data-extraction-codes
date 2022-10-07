from os import device_encoding, name
from re import template
import pandas as pd
import code128
from numpy import column_stack, nan
from PIL import Image, ImageFont, ImageDraw 
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep

#########################

device ="Haylou T15 Black"
imei = [20912687692]
adet=15000
forname = 'T15B'
deviceNameAlligment = 60

#########################

for j in range (adet-1):
    imei.append(imei[j]+1)
for m in range(len(imei)):
    imei[m]=forname+str(imei[m])

df = pd.DataFrame(imei)
writer = pd.ExcelWriter("C:/Users/inci1/Desktop/"+device+".xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()