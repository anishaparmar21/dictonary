i=0
a={}
while i<5:
    name=input("enter the name:")
    marks=int(input("enter the number:"))
    a.update({name:marks})
    i+=1
print(a)