f = []
for (dirpath, dirnames, filenames) in walk("C:/Users/inci1/Desktop/upload"):
    f.extend(filenames)
    break

sheetMerger = PdfFileMerger()

for j in range (len(f)):
    mergedObject.append(PdfFileReader("C:/Users/inci1/Desktop/upload/"+f[j], 'rb'))
    mergedObject.write("C:/Users/inci1/Desktop/upload/liste.pdf")

