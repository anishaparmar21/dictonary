dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
a={}
for i in dic.items():
    if i not in a:
        a.update(dic)
print(a)





         