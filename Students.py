students = {}

def add_student(roll, name):
    students[roll] = name
    return "Student Added"

def remove_student(roll):
    if roll in students:
        del students[roll]
        return "Student Removed"
    return "Student Not Found"

def search_student(roll):
    return students.get(roll, "Student Not Found")

def update_student(roll, name):
    if roll in students:
        students[roll] = name
        return "Student Updated"
    return "Student Not Found"
