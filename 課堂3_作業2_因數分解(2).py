numIN = int(input("輸入一個數字做因式分解："))
count = 0
print("{}=".format(numIN),sep="",end="")

for i in range(2,numIN):
    
    while numIN % i == 0:
        
        numIN //= i
        count +=1
        if count > 1:
            print("x",sep="",end="")
        
        print(i,sep="",end="")

if count == 0 :
    print("1X{}，這個數是質數。".format(numIN))
    
