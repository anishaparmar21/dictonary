dic={'a':{'b':45},'c':56,'d':34,'f':{'e':10}}
sum=0
for i in dic:
    if type(dic[i])==dict:
        for j in dic[i]:
            sum+=dic[i][j]
    else:
        sum+=dic[i]
print("sum","=",sum)     