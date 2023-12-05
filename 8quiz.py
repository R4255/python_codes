import copy
from heapq import heappush,heappop
n=3
row=[1,0,-1,0]
column=[0,-1,0,1]
class priorityqueue:
    def __init__(self):
        self.heap=[]
    def push(self,k):
        heappush(self.heap,k)
    