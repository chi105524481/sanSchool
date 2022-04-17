#課堂3_作業4
#有一個分數序列 ： 2/1 ,3/2 ,5/3 ,8/5 ,13/8 , 21/13 求這個數列的前20項和 

data = [1]
s = 0
i = 1
data2 = [0]

for x in range(0,20):
    i = data[x] +data[x-1]
    data.append(i)

print(data)

for y in range(1,len(data)):
    j = data[y] / data[y-1]
    data2.append(j)
    #print(data[y],"/",data[y-1],"=",j)

for z in range(1,len(data2)):
    s = s +data2[z]

print()
print(s)
print(sum(data2))