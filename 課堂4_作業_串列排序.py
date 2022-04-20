#作業一
#用for來處理
#data = [100,80,90,70,59,30,21,35]
#請排序它，從小到大
#請排序，從大到小
#--------------------------------------------------------
#作業二
#data = [10,20,30,25,50,60]
#請反轉內容 ==>[60,50,25,30,20,10]
#--------------------------------------------------------
data = [100,80,90,70,59,30,21,35]
data_FromBig = []
L = len(data)

for i in range(L):
    L = len(data)
    Max = data[0]
    for j in range(L):
        if data[j] > Max :
            Max = data[j]
            
    data_FromBig.append(Max)
    data.remove(Max)
    
print("大到小排序：",data_FromBig)
############################################################    
data_1 = [100,80,90,70,59,30,21,35]
data_FromSmall = []           
L_1 = len(data_1)

for i in range(L_1):
    L_1 = len(data_1)
    Min = data_1[0]
    for j in range(L_1):
        if data_1[j] < Min :
            Min = data_1[j]
            
    data_FromSmall.append(Min)
    data_1.remove(Min)
    
print("小到大排序：",data_FromSmall)        
#############################################################
data_2 = [10,20,30,25,50,60]
data_change = []
L_3 = len(data_2)

for i in range(L_3 // 2):
    data_2[i],data_2[L_3-1-i] = data_2[L_3-1-i],data_2[i]
    
print("內容反轉：",data_2)








