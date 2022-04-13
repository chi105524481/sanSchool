n = int(input("輸入一個數字，得到此數字以下的質數； "))

for i in range(2,n+1):
    
    for j in range(2,i):
        
        if (i % j == 0):
            break
        
    else:
        print(i,end=" , ")
        


        