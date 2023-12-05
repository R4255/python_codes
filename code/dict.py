#d={}
#l = int(input("enter the length of the dictionary:"))
#for x in range(l):
#    print("x:",x)
#    key=input("enter key:")
#    value=input("enter value:")
#    #d[key]=value
#    a={key:value}
#    d.update(a)
#print(d)
#print("=============================================")
#dict={1:"rohit",2:"gupta",3:"rohit gupta"}
#print(dict[2])
#dict={rollno.:["name",marks]}

dict={}
for i in range(5):
    list=[]
    name=(input("enter your name:"))
    marks=int(input("enter your marks:"))
    list.append(name)
    list.append(marks)
    dict[i]=list
    print(dict)