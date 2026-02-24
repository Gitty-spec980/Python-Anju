student_data = {
    "Anjali": (12, "Student"),
    "Aarya": (12, "Younger sister"),
    "Deepali mam": (34, "Our teacher.")
}


key = input("Enter persons name ").strip()


if key in student_data:
    
    age, major = student_data[key]
    print(f" Found: {key} is {age} years old and is {major}.")
else:
    print(" Key not found in the dictionary.")