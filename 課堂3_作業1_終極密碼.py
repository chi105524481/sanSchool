#終極密碼 
#由系統亂數 1~100 之間的值，由使用者來猜
#每次猜都能顯示新的縮小範圍

import random

start = 1
end = 100

number = random.randint(1,100)
guess = int(input("終極密碼，請輸入1~100的值："))

while  number != guess :
    if number > guess :
        start = guess
        print(start,"與",end,"之間")
        guess = int(input("再猜："))
        
    else:
        end = guess
        print(start,"與",end,"之間")
        guess = int(input("再猜："))
        
print("恭喜猜到答案：",guess)










