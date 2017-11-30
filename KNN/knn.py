import xlrd
import math

file_location = "Dataset Tugas 3 AI 1718.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
sheet2 = workbook.sheet_by_index(1)

# print("data training")
# for i in range(sheet.nrows):
#     for j in range(sheet.ncols):
#         print(sheet.cell_value(i,j), end=' ')
#     print()
#
# print("data test")
# for i in range(sheet2.nrows):
#     for j in range(sheet2.ncols):
#         print(sheet.cell_value(i,j), end=' ')
#     print()
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

def pisah(arr):
    idx = int(len(arr)/2)
    return arr[0:idx],arr[idx:len(arr)]
    return result

def merge(arr1,arr2):
    idx1=0
    idx2=0
    ret = []
    for i in range(len(arr1)+len(arr2)):
        if idx2 >= len(arr2) or (idx1 < len(arr1) and arr1[idx1]<arr2[idx2]):
            ret.append(arr1[idx1])
            idx1 = idx1+1
        else:
            ret.append(arr2[idx2])
            idx2 = idx2+1
    return ret

def merge_sortiungeuy(arr):
    if len(arr) < 2:
        return arr
    temp = pisah(arr)
    return merge(merge_sortiungeuy(temp[0]),merge_sortiungeuy(temp[1]))


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
    e = merge_sortiungeuy(z)
    f = e[0:3]
    g = z.index(f[0])
    for k in range(2):
        if(n1[g]==1.0):
            hoax = hoax+1
        else:
            tidak = tidak+1

    if hoax>=tidak:
        n2[i] = 1.0
        print("nilai:", i, "->","hoax")
    else:
        n2[i] = 0.0
        print("nilai:", i, "->", "tidak hoax")








    #print("nilai:",i,";",n2[i])

    # arr = np.array(a)
    # print(arr)
    #print(i)
    #print(f)
    #print(f)








    # for k in range(2):
    #     print(z.index(e[k]))








#     for i in range(1, sheet.nrows):
#         x1.append(sheet.cell_value(i, 1))
#         y1.append(sheet.cell_value(i, 2))
#         k1.append(sheet.cell_value(i, 3))
#         c1.append(sheet.cell_value(i, 4))
#
# def test():
#     for i in range(1, sheet2.nrows):
#         x2.append(sheet2.cell_value(i, 1))
#         y2.append(sheet2.cell_value(i, 2))
#         k2.append(sheet2.cell_value(i, 3))
        #c2.append(sheet2.cell_value(i, 4))












