grades = {
    "Aarya": 88,
    "Amma": 73,
    "Nanna": 95,
    "Deepali Mam": 64,
    "Anjali": 80
}
total = 0
for name in grades:
    total = total + grades[name]

average = total / len(grades)
print("Class average:", average)
top_name = ""
top_score = 0

for name in grades:
    if grades[name] > top_score:
        top_name = name
        top_score = grades[name]

print("Highest score:", top_name, top_score)
lookup = input("Look up a student: ")
score = grades.get(lookup, "Not found")
print("Score:", score)