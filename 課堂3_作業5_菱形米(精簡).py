layer = int(input("請輸入層數(奇數)："))
mid = layer // 2 +1

for i in range(mid+1):
    print(" "*(mid-i),"*"*(2*i-1))
    
for j in range(mid-1,0,-1):
    print(" "*(mid-j),"*"*(2*j-1))
