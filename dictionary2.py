# test_dict= {'Codingal' : 2, 'is' : 2, 'Best' : 2, 'for' :2, 'Coding' :1}
# print("The original dictionary : " + str(test_dict))
# k=2

# count = 0
# for key in test_dict:
#     if test_dict[key] == k:
#         count+=1


# print("Frequency of K is : " +str(count))

student_data = {
    "id1": {"name": "Sara", "class": "5", "subject": "ELA, Math, Science"},
    "id2": {"name": "David", "class": "5", "subject": "ELA, Math, Science"},
    "id3": {"name": "Sara", "class": "5", "subject": "ELA, Math, Science"},
    "id4": {"name": "Surya", "class": "5", "subject": "ELA, Math, Science"}


}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details

for k, v in result.items():
    print(k, ":", v)
