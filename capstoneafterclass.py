def intro():
    print('WHATS UR NAME CALCULATOR MASTER?!!!')
    global name
    name = input()
    print(name + ', WELCOME TO THE MATH DUNGEON!!!')
    print('1. SUM (+) \n2. DIFFERENCE (-) \n3. PRODUCT (*) \n4. AVERAGE (/)')
    print('CHOOSE YOUR DESTINY (1-4) BEFORE I SEND U TO PLUTOOOOO!!!')

def calculate():
    choice = input('PUT YOUR CHOICE HERE RIGHT NOWWWW: ')
    

    nums = []
    print('ENTER YOUR NUMBERS ONE BY ONE. TYPE "STOP" WHEN YOU ARE DONE OR BE DOOMED!!!')
    
    while True:
        val = input('GIVE ME A NUMBERRRRR: ')
        if val.upper() == "STOP":
            break
        try:
            nums.append(float(val))
        except:
            print("THAT IS NOT A NUMBER U SILLY GOOSE! TRY AGAINNNNN")

    count = len(nums)
    
    if count == 0:
        print("YOU GAVE ME NOTHING!!! MATH CANNOT BE DONE!!!")
        return

    
    if choice == '1':
        result = sum(nums)
        op_name = "TOTAL SUM"
    elif choice == '2':
        result = nums[0]
        for n in nums[1:]:
            result -= n
        op_name = "ULTIMATE DIFFERENCE"
    elif choice == '3':
        result = 1
        for n in nums:
            result *= n
        op_name = "PRODUCT"
    else:
        print("THAT WAS NOT AN OPTION! YOU HAVE FAILED ME!!!")
        return

    print('\n--- RESULTS  ---')
    print('HEY {}, YOUR {} IS {}!!!'.format(name, op_name, result))
    print('YOU DARED TO ENTER {} NUMBERS!!!'.format(count))

playagain = 'yes'
while playagain.lower() in ["yes", "y"]:
    intro()
    calculate()
    print("\nDO YOU WANT TO CALCULATE AGAIN U FILTHY ANIMAL? (yes/no)")
    playagain = input()
