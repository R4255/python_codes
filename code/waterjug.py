#water jug problem 
from collections import defaultdict
jug1,jug2,aim=4,3,2
visited=defaultdict(lambda:False)
def waterjugproblem(amt1,amt2):
    if(amt1==aim and amt2==0) or (amt2==aim or amt1==0):
        print(amt1,amt2)
        return True
    if visited[(amt1,amt2)]==False:
                print(amt1,amt2)
                visited[(amt1,amt2)]=True
                return waterjugproblem(amt1,0) or waterjugproblem(0,amt2) or waterjugproblem(jug1,amt2) or waterjugproblem(amt1,jug2) or waterjugproblem(amt1+min(amt2,(jug1-amt1)),amt2-min(amt2,(jug1-amt1))) or waterjugproblem(amt1-min(amt1,(jug2-amt2)),amt2+min(amt1,(jug2-amt2)))
    else:
        return False
    print("steps")
    #now here we call the function 
if __name__=="__main__":
       waterjugproblem(0,0)
           