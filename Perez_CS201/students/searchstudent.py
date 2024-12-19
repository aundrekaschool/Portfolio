class SearchStudent:
    def __init__(self, students):
        """
        Initialize the SearchStudent class with a Student instance.
        :param students: Instance of the Student class containing student data.
        """
        self.students = students

    def search_student(self, idnum):
        print(f"Searching for ID: {idnum}")  # Debug line
        for student in self.students.allstudents:
            print(f"Checking ID: {student[2]}")  # Debug line
            if student[2].strip() == idnum.strip():  # Ensure no whitespace issues
                print(f"Found student: {student}")  # Debug line
                return student
        print("Student not found.")  # Debug line
        return None

    def verify_login(self, idnum):
        """
        Verify if the provided ID number corresponds to a registered student.
        :param idnum: ID number of the student.
        :return: Student information if the ID is valid, otherwise False.
        """
        for student in self.students.allstudents:
            if student[2] == idnum:  
                return student  # Return student details if login is valid
        return False  # Return False if login fails
