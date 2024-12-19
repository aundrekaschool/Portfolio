class Student:
    def __init__(self, file="student_data.txt"):
        self.name, self.age, self.idnum, self.email, self.phone = " ", " ", " ", " ", " "
        self.allstudents = []
        self.file = file
        self.load()  # Load the data from the file when the class is initialized

    def load(self):
        seen_ids = set()
        self.allstudents.clear()  # Clear the existing list before loading new data
        try:
            with open(self.file, "r") as file:
                for line in file:
                    student_data = line.strip().split(", ")
                    if len(student_data) == 5 and "-" in student_data[2]:
                        if student_data[2] not in seen_ids:
                            self.allstudents.append(student_data)
                            seen_ids.add(student_data[2])  # Track IDs
                        else:
                            print(f"Duplicate ID found: {student_data[2]}")
            print("Loaded students:", self.allstudents)
        except FileNotFoundError:
            print(f"{self.file} not found. Starting with an empty student list.")
