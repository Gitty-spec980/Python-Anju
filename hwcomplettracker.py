ttl_hw = 4
org_count = ttl_hw
print(f"You have {org_count} pages of homework to do currently! \n" )

comp_count = 0
task_numb = 1

while task_numb <= ttl_hw:


    if task_numb == 1:
        next_task= "Math Paper"
    elif task_numb==2:
        next_task= "English Paper"
    elif task_numb==3:
        next_task= "Science Paper"
    else:
        next_task= "Social studies Paper"

    ans = input(f"Did you finish {next_task}? (Y/N) ")


    if ans=="Y":
        comp_count += 1
        task_numb += 1
        print("Satisfiying!! one!! !st homework page, done")
    else:
        print(" AWWWW. It's okay just lock in and finish it heheheh")

    print("Amount of Homework pages left: ", ttl_hw - comp_count)
    print()

print("  OMGGG YOU FINISHEEDDDD GREAT JOBB!! HOMEWORK PAGES FINISHEDD!!")

print("Now lets look at an infinite loop")

test_val=0
saftey_counter=0

while test_val <=0:
    print("Stopping here on purpose to show that a real infinite loop never stawps on its ownn!")
    break
print("\n HW COMPLETETION SUMMARIZATIONN:")
print("Homework that was assigned today:", org_count)
print("Homework that was completed today:", comp_count)
print("Homework that is reaming/left today:", ttl_hw - comp_count)






