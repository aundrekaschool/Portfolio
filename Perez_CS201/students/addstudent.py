class AddStudent:
    def __init__(self, student):
        self.students = student

    def add(self, name, age, idnum, email, phone):
        if self.is_duplicate(idnum, email):
            print(f"Duplicate detected: A student with ID {idnum} or email {email} already exists.")
            return
        # Directly append the new student data to the list of all students
        student_data = [name, age, idnum, email, phone]
        self.students.allstudents.append(student_data)
        print(f"Added student {student_data[0]} to the list.")
        self.write_to_file(student_data)  # Write the new student data to the file

    def is_duplicate(self, idnum, email):
        # Check if the student ID or email already exists in the list
        for student in self.students.allstudents:
            if student[2] == idnum or student[3] == email:
                return True
        return False

    def write_to_file(self, student_data):
        # Write the student data to the file
        with open(self.students.file, "a+") as file:
            file.write(f"{', '.join(student_data)}\n")
        print("Data saved successfully")
