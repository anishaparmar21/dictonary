dict ={'a':50, 'b':58,'c':56,'d':40, 'e':100, 'f':20}
max=0
for i in dict:
    if dict[i]>max:
       key1=i
       max=dict[i]
# dict[i]=max
print(max)   
max1=0
for i in dict:
    if dict[i]>max1 and dict[i]!=max:
        key2=i
        max1=dict[i]
# dict[i]=max1
print(max1)
max2=0
for i in dict:
    if dict[i]>max2 and dict[i]!=max and dict[i]!=max1:
        key3=i
        max2=dict[i]
# dict[i]=max2
print(max2)
print(key1,key2,key3)