
for i in range(2,100):
    x = 0
    
    for j in range(2,i):
        
        if (i % j == 0):
            x += 1
        
    if (x < 1):
        print(i,end=" , ")
        


        