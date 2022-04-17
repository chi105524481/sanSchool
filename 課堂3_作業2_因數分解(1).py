"""
課堂3_作業2_因數分解
當使用者輸入：720
要印出：720 = 2X2X2X2X3X3X5
"""

x = 0

num_in = int(input("輸入一個數字產生因數分解："))
print(num_in,"=",sep='',end="")
for i in range(2,num_in):
    
    for j in range(2,num_in):

        if num_in % j == 0 :
            
            if x > 0:
                print("X",sep='',end='')
            
            print(j,sep='',end='')
            num_in = num_in // j
            x += 1
            break
        
if x == 0 :
    print("1X",num_in,",是質數。",sep="")


            
        
    


            
        
            
    
    
    
        
        

    
        


            
    