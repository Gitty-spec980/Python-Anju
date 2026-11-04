set1={"mango", "pineapple", "apples", "blueberries", "orange"}
set2={"pineapple","bannanas", "green apple", "mango","papaya"}
set1=set1.intersection(set2)
print(set1)
import array as arr
fruit_counts=arr.array( "i",[3,5,2, 4])
print("Fruit counts array: ", fruit_counts)

fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit counts after adding items: ", fruit_counts)

count_4=fruit_counts.count(4)
print("Number of times 4 appears:", count_4)

fruit_counts.reverse()
print("Reversed fruit counts array: ", fruit_counts)