import random

start = 1
end = 100

number = random.randint(1,100)
guess = int(input("終極密碼，請輸入1~100的值："))

while  number != guess:
    if (number > guess and start < guess < end):
        start = guess
        print(start,"與",end,"之間")
        guess = int(input("再猜："))
        
    elif(number < guess and start < guess < end):
        end = guess
        print(start,"與",end,"之間")
        guess = int(input("再猜："))
        
    else:
        print("輸入值不在{}~{}之間".format(start, end))
        guess = int(input("再猜："))
        
print("恭喜猜到答案：",guess)
