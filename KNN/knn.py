import xlrd
import math

file = xlrd.open_workbook("wew.xlsx")
sheet = file.sheet_by_index(0)
sheet2 = file.sheet_by_index(1)

x1 = []
x2 = []
y1 = []
y2 = []
k1 = []
k2 = []
c1 = []
c2 = []
n1 = []
n2 = []
sihoax = []

def cari_jarak(x1,x2,y1,y2,k1,k2,c1,c2):
    a = (x1-x2)**2 + (y1-y2)**2 + (k1-k2)**2 + (c1 - c2)**2
    akar = math.sqrt(a)
    return akar

for i in range(1,sheet.nrows):
     x1.append(sheet.cell_value(i,1))
     y1.append(sheet.cell_value(i,2))
     k1.append(sheet.cell_value(i,3))
     c1.append(sheet.cell_value(i,4))
     n1.append(sheet.cell_value(i,5))

for i in range(1,sheet2.nrows):
     x2.append(sheet2.cell_value(i,1))
     y2.append(sheet2.cell_value(i,2))
     k2.append(sheet2.cell_value(i,3))
     c2.append(sheet2.cell_value(i,4))
     n2.append(sheet2.cell_value(i,5))
     sihoax.append(sheet2.cell_value(i, 5))




wow = []
for i in range(len(x2)):
    z=[]
    a=[]
    e=[]
    g=[]
    hoax = 0
    tidak = 0
    for j in range(len(x1)):
        a= cari_jarak(x1[j],x2[i],y1[j],y2[i],k1[j],k2[i],c1[j],c2[i])
        z.append(a)
    best = sorted(z)[0:3]

    for k in best:
        if n1[z.index(k)] == 1.0:
            hoax+=1
        else:
            tidak+=1
    if hoax>tidak:
        n2 = 1.0
    else:
        n2 = 0.0
    wow.append(n2)
    print(n2)
count = 0
for i in range(len(x2)):
     if(wow[i]==sihoax[i]):
         count+=1

akurasi  = (count/len(x2))*100
print("akurasi",akurasi,"%")