#in binary search the list or the array has to be sorted
import random
def binarysearch(l,element):
    start=0
    end=len(l)-1
    while start<end:
        mid=(start+end)//2
        if l[mid]==element:
            return mid
        elif l[mid]>element:
            end=mid-1
        elif l[mid]<element:
            start=mid+1
    return -1
if __name__=="__main__":
    l=[]
    for i in range(20):
        k=random.randint(1,50)
        l.append(k)
    l.sort()
    print(l)
    tt=int(input("enter any no. you want to search::"))
    print(binarysearch(l,tt))

