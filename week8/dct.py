student={
    "name":"manoj",
    "age": 21,
    "course":"b.tech"
}
print(student.keys())
print(student.values())
print(student.items())
student.pop("age")
print("after pop",student)
del student["course"]
print("after delete",student)
