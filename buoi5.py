#Bai1
#a
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
print(friends[:4])
#b
print(friends[-4:])
#c
print(friends[::-1])
#d
print(friends[1:])
#e
new = friends[:]
print(new == friends)
print(new)
#f
print(friends[2:-1])

#Bai2
#a
students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
student_1 = students[0]
print(student_1)
#b
student_id = student_1[0]
student_name = student_1[1]
student_age = student_1[2]

print(f"ID: {student_id}, name: {student_name} - age: {student_age}")

#c
new_students = students[-2:]
print(new_students)

#d
student3_id = students[-1][0]
print(student3_id)