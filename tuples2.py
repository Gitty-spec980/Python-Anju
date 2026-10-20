# tuplex=("Hello",55,0.123,True)
# tuplex2=(2,4,8,10,12,14) + (9,)
# print(tuplex2)
# tuple1=(4,8,7,4,9,3,4,6,5,4,4)
# # print(tuple1.count(4))
# print(tuple1[3:5])

def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,3,2,1)

if(palind(r)):
    print("The tuple is flip-flop!")
else:
    print("The tuple is not flip-flop!")

