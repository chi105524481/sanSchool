"""
   *
  *** 
 *****
*******
 *****
  ***
   *
"""

layer = int(input("請輸入層數(奇數)："))
mid = layer // 2 +1
star = 1

for space in range(mid,1,-1):
    print(" "*space,end="")
    
    while star <= layer :
        print("*"*star)
        break
    star += 2
    
for space in range(1,mid+1):
    print(" "*space,end="")
    while star > 0 :
        print("*"*star)
        break
    star -=2
        