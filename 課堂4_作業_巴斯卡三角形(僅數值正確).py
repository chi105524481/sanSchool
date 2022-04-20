data = [1]
data2 = []

for i in range(6):
    L = len(data)
    data2.append(1)
    
    for j in range(L):
        if j < L-1 :
            c = data[j]+data[j+1]
            data2.append(c)
            
    data2.append(1)
    data = data2
    print(data)
    data2 = []
