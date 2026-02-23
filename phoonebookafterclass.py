import sys
55
def initial_slambook():
    rows, cols = int(input("Please enter initial number of answers(5 answers only):")), 5


    slam_book = []
    print(slam_book)
    for i in range(rows):
        print("\nEnter answers %d details in the following order (ONLY):"%(i+1))
        print("NOTE: *indicates mandatory fields")
        print("......................................")
        temp = []
        for j in range(cols):


            if j==0:
                temp.append(str(input("Enter name*:")))


                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting ue to blank field...")

            if j== 1:
                temp.append(int(input("Enter favorite hobby*:")))

            if j== 2:
                temp.append(str(input("Enter favorite color*:")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None


            if j== 3:
                temp.append(str(input("Enter your favorite motto in life*:")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j== 4:
                temp.append(str(input("Enter 1 word that describes you*:")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        slam_book.append(temp)

    print(slam_book)
    return slam_book

def menu():
    print("*********************************************")
    print("\t\t\tSLAMBOOK")
    print("*********************************************")
    print("\tConfused? Then check this are to do things for your slambook\n")
    print("1. Remove your answers to a question")
    print("2. Delete all answers")
    print("3. Search for your answers")
    print("4. Display your answers to the questions")
    print("5. Exit Slambook")

    choice = int(input("Please enter your choice:"))
    return choice

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i ==0:
            dip.append(str(input("Name:")))
        if i ==1:
            dip.append(int(input("Favorite hobby:")))
        if i ==2:
            dip.append(str(input("Favorite color:")))
        if i==3:
            dip.append(str(input("Your favorite motto in life")))
        if i ==4:
            dip.append(str(input("1 word that describes you:")))
    pb.append(dip)

    return pb
    
def remove_existing(pb):

    query = str(input("Do you wantto remove your answer? Please enter the answer you want to remove"))
    
    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp+= 1

            print(pb.pop(i))
            print("This answer has now been removed")

            return pb
        
    if temp == 0:
        print("Sorry your answer could not be detected\nPlease recheck and try again later.")
        return pb
    
def delete_all(pb):
    return pb.clear

def search_existing(pb):
    choice = int(input("Enter search criteria\n\n\n 1.Name\n2. Favorite Hobby\n3. Favorite Color\n4. Favorite Motto in life\n5. 1 word to describe you\ \nPlease enter:"))

    temp = []
    check = -1

    if choice == 1:
        query = str(input("Please enter name you wish to search:"))
        for i in range(len (pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = int(input("Please enter your favorite hooby to search for:"))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i   
                temp.append(pb[i])

    elif choice == 3:
        query = str(input("Please enter your favorite color to search:"))    
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        query =str(input("Please enter your favorite motto for life to search for:"))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    elif choice == 5:
        query = str(input("Please enter one word to describe you to search:"))
        if query == pb[i][4]:
            check = i
            temp.append(pb[i])

    else:

        print("BEEP_BEEP INVALIDDD")
        return -1


    if check == -1:
        return -1
    else:
        display_all(temp)
        return check

def display_all(pb):
    if not pb:

        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])

def thanks():
    print("******************************************")
    print("THY SOOO MUCH ! I NOW KNOW SO MUCH ABOUT YOU")
    print("Please visit us again")
    print("******************************************")
    sys.exit("Byee, Have a nice day!")


print("................................................")
print("WELCOMEEE")
print(".................................................")


ch = 1
pb=initial_slambook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("This answer does not exist Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()