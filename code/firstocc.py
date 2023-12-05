def firstocc(l,element):
    for i in range(len(l)):
        if l[i]==element:
            return i
    return -1
if __name__=="__main__":
    l=[231,12351,31,151,31251,12,1,1,11443,5436326,426]
    print(firstocc(l,1))
    