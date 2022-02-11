dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
a={}
for i in dic1:
    a.update(dic1)
    a.update(dic2)
    a.update(dic3)
print(a)
    