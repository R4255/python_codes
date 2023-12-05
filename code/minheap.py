class minheap:
    def __init__(self):
        self.arr=[]
    def parent(self,i):
        return (i-1)//2
    def lchild(self,i):
        return 2*i+1
    def rchild(self,i):
        return 2*i+2
    def insert(self,x):
        arr=self.arr
        arr.append(x)
        i=len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]#in this step we swap parent and the child 
            i=p
