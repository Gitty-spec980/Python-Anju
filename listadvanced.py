# l=[2,5,8,10,6]
# print("Original List is: ",l)
# sum=0
# for i in l:
#     sum=sum+i
# print(" The sum is: ", sum)
# print("The average is: ", sum/len(l))
# l.sort()
# print(l)

# print("Smallest Value present: ", min(l))
# print("Largest Value present: ", max(l))


# #Second method to sort out large/small values
# # print("Min Value ",l[0])
# # print("Max Value ",l[-1])


def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("List of words with first and last character same\n ", lst)
    return ctr

count=match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having first and last character same: ", count)
