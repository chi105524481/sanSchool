#有四個數字 1,2,3,4 能組成多少的互不相同且無重複數字的三位數，各是多少?
#例如 123  124

data = [1,2,3,4]
n = 0
for x in range(0,4):
    for y in range(0,4):
        if y != x:
            for z in range(0,4):
                if z != y and z != x:
                    print(data[x],data[y],data[z],sep="",end=",")
                    n += 1
                
print()               
print("共有{}種組合".format(n))
            
      