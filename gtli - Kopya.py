from os import name
from re import template
import pandas as pd
from numpy import column_stack, nan

imei = 2384522024

barkod = []

for i in range(199):

    barkod.append('RT2SW'+str(imei))
    
    imei= imei+1

with open(r'C:/Users/inci1/Desktop/liste.txt', 'w') as filehandle:
    for listitem in barkod:
        filehandle.write('%s\n' % listitem)
print(barkod)
