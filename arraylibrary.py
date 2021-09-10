import random
arr=[]
size=int(input("size:"))


def initArray(arr,size):
    for i in range(size):
        arr.append(random.randint(1,10))
def initArrayWithRange(arr,size,arange,brange):

    for i in range(size):
        arr.append(random.randint(arange,brange))
    print(arr)
def initArrayWithInput(arr,size):

    for a in range(size):
        arr.append(a)
    print(arr)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

def printArray(arr, styleID):
    for i in range(size):
        arr.append(random.randint(10,20))
    print(arr)
    if styleID==1:
        print(bcolors.OKCYAN+bcolors.BOLD,arr)
    elif styleID==2:
        for i in arr:
            print(bcolors.OKGREEN+bcolors.UNDERLINE,i,end=" ")
arr2=[]
def sizeOfNegatives(arr2):
    for j in range(size):
        arr2.append(random.randint(-10,10))
    s=0
    for i in arr2:
        if i<0:
            s+=1

    return s

def sizeOfPositives(arr2):
    for j in range(size):
        arr2.append(random.randint(-10,10))
    p=0
    for i in arr2:
        if i>0:
            p+=1

    return p
a=[]
def getPositives(arr2):
    for i in range(size):
        arr2.append(random.randint(-10,10))
    for i in arr2:
        if i>0:
            a.append(i)
    return a
b=[]
def getNegatives(arr2):
        for i in range(size):
            arr2.append(random.randint(-10,10))
        for i in arr2:
            if i<0:
                b.append(i)
        return b

def  checkSortable(arr2):
            for i in range(size):
                arr2.append(random.randint(1,5))
            print(arr2)
            isSorted=True
            for i in range(size-1):
                if (arr2[i]>arr2[i+1]):
                    isSorted= False
            return isSorted
def sortArray(arr2, typeSort):
    for i in range(size):
        arr2.append(random.randint(1,5))
    print(arr2)
    if typeSort==1:
        for i in range(len(arr2)-1):
            for j in range(i+1,len(arr2)):
                if arr2[i]>arr2[j]:
                    temp=arr2[i]
                    arr2[i]=arr2[j]
                    arr2[j]=temp
        print(arr2)
    elif typeSort==2:
        for i in range(len(arr2)-1):
            for j in range(i+1,len(arr2)):
                if arr2[i]<arr2[j]:
                    temp=arr2[i]
                    arr2[i]=arr2[j]
                    arr2[j]=temp
        print(arr2)
    else:
        print("natija yo'q")
def changeMinMax(arr2):
    for i in range(size):
        arr2.append(random.randint(1, 10))
    print(arr2)

    min_m = arr2[0]
    max_m = arr2[0]
    for i in arr2:
        if i < min_m:
            min_m = i
        if i > max_m:
            max_m = i

    temp=min_m
    arr2[arr2.index(min_m)]=max_m
    arr2[arr2.index(max_m)]=temp
    return arr2

massiv=[23,23,2,23,13,24,13,14,0]
def updateArray(arr2,value,newValue):
    arr2[arr2.index(value)]=newValue
    print(arr2)









