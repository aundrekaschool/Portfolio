import tkinter as tk
from tkinter import ttk
from student import Student
from addstudent import AddStudent
from searchstudent import SearchStudent

# Initialize objects
stu = Student()
addstud = AddStudent(stu)
search = SearchStudent(stu)

# Create the main window and other widgets after the styles are set
win = tk.Tk()
win.geometry("1920x1080")
win.title("Student Information System")
win.config(bg="#fce4ec")

attempts = 0

# Define styles
# Define styles
# Define styles
style = ttk.Style()

# Style definitions
style.configure("Login.TFrame", background="#fce4ec")
style.configure("Login.TLabel", background="#fce4ec", foreground="#880e4f", font=("Arial", 24, "bold"))
style.configure("Login.TEntry", foreground="#880e4f", padding=(20, 20), height=30)
style.configure("Login.TButton", background="#f8bbd0", foreground="#880e4f", font=("Arial", 20), relief="raised", padding=(10, 5))
style.configure("Navbar.TFrame", background="#fce4ec")
style.configure("Navbar.TButton", background="#fce4ec", foreground="#880e4f", font=("Arial", 20), relief="flat", width=40, height=2, padding=(10, 20))
style.configure("Content.TFrame", background="#ffffff")
style.configure("Content.TLabel", font=("Arial", 16), background="#ffffff", foreground="#880e4f")
style.configure("Content.TLabelError", font=("Arial", 16, "bold"), background="#fce4ec", foreground="#d32f2f")  # For error messages in pink theme


# Rest of the code...

# Login frame
login_frame = ttk.Frame(win, style="Login.TFrame")
login_frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_id = ttk.Label(login_frame, text="Enter Student ID:", style="Login.TLabel")
lbl_id.pack(pady=40)

entry_id = ttk.Entry(login_frame, style="Login.TEntry",  width=50, font=("Arial", 17))
entry_id.pack(pady=40)

btn_login = ttk.Button(login_frame, text="Login", command=lambda: login(entry_id.get()), style="Login.TButton")
btn_login.pack(pady=40)

lblError = ttk.Label(login_frame, text="", style="Login.TLabel")
lblError.pack(pady=0)

# Main frame for the menu
main_frame = ttk.Frame(win, style="Login.TFrame")

# Function to create navigation bar
def create_navbar(idnum):  # Pass idnum to the navbar function
    left_frame = ttk.Frame(main_frame, style="Navbar.TFrame", width=400)
    left_frame.pack(side="left", fill="y", padx=20, pady=20)

    # Pass the idnum to the display_student_info function
    btn_view_info = ttk.Button(left_frame, text="View your information", command=lambda: display_student_info(idnum), style="Navbar.TButton")
    btn_view_info.pack(pady=20)
    
    btn_view_other_info = ttk.Button(left_frame, text="View other student's information", command=lambda: show_content("view_other_info"), style="Navbar.TButton")
    btn_view_other_info.pack(pady=20)

    btn_register_student = ttk.Button(left_frame, text="Register a New Student", command=lambda: show_content("register_student"), style="Navbar.TButton")
    btn_register_student.pack(pady=20)

    btn_print_all = ttk.Button(left_frame, text="Print all students", command=lambda: show_content("print_all"), style="Navbar.TButton")
    btn_print_all.pack(pady=20)

    btn_exit = ttk.Button(left_frame, text="Exit", command=win.quit, style="Navbar.TButton")
    btn_exit.pack(pady=20)


# Function to handle dynamic content display
def show_content(content):
    # Clear the content frame to remove existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Initialize the `text` variable to avoid the UnboundLocalError
    text = ""

    # Handle different content views
    if content == "view_info":
        text = "Displaying your information..."
        display_student_info()  # Call function to display student info
    elif content == "view_other_info":
        text = "Searching for other student's information..."
        view_other_student_info()  # Function to search for other students
    elif content == "register_student":
        text = "Registering a new student..."
        register_student()  # Function for registering a new student
    elif content == "print_all":
        text = "Printing all students..."
        view_all_students()  # Function to print all student information
    else:
        text = "Unknown action."

    # Create a label to display the action text
    ttk.Label(content_frame, text=text, style="Content.TLabel", font=("Arial", 28, "bold")).pack(pady=30)

    # Optional decorative label at the bottom
    design = ttk.Label(content_frame, text="･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f")
    design.pack(pady=10)


# Content frame for displaying student info
content_frame = ttk.Frame(main_frame, style="Content.TFrame")
content_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Define function to display student info
def display_student_info(idnum):
    student = search.search_student(idnum)  # Retrieve the student info

    if student and isinstance(student, list):  # Ensure `student` is a list
        # Clear the content frame
        for widget in content_frame.winfo_children():
            widget.destroy()

        # Decorative title for the "Your Information" section
        ttk.Label(content_frame, text="Your Information", style="Content.TLabel", font=("Arial", 32, "bold"), foreground="#880e4f").pack(pady=20)

        # Add a decorative line or separator
        ttk.Label(content_frame, text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f").pack(pady=10)

        # Display student's information with added styling
        ttk.Label(content_frame, text=f"Name: {student[0]}", style="Content.TLabel", font=("Arial", 18), foreground="#333333").pack(pady=10)
        ttk.Label(content_frame, text=f"Age: {student[1]}", style="Content.TLabel", font=("Arial", 18), foreground="#333333").pack(pady=10)
        ttk.Label(content_frame, text=f"Student ID: {student[2]}", style="Content.TLabel", font=("Arial", 18), foreground="#333333").pack(pady=10)
        ttk.Label(content_frame, text=f"Email: {student[3]}", style="Content.TLabel", font=("Arial", 18), foreground="#333333").pack(pady=10)
        ttk.Label(content_frame, text=f"Phone: {student[4]}", style="Content.TLabel", font=("Arial", 18), foreground="#333333").pack(pady=10)

        # Add a decorative line or separator at the bottom
        ttk.Label(content_frame, text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f").pack(pady=10)

        # Optional decorative label at the bottom of the section
        design = ttk.Label(content_frame, text="･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f")
        design.pack(pady=10)
    else:
        # Student not found or returned an invalid format
        for widget in content_frame.winfo_children():
            widget.destroy()
        ttk.Label(content_frame, text="Student not found.", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#d32f2f").pack(pady=20)



def view_other_student_info():
    # Create a frame to enter the student ID
    search_frame = ttk.Frame(content_frame, style="Content.TFrame")
    search_frame.pack(pady=30)

    # Label for input
    ttk.Label(search_frame, text="Enter Student ID to search:", style="Content.TLabel").pack(pady=10)

    # Entry field for student ID
    entry_search_id = ttk.Entry(search_frame, style="Login.TEntry", font=("Arial", 16), width=30)
    entry_search_id.pack(pady=10)

    # Function to perform the search and display results
    # Define function to display search results
    def search_and_display():
        search_id = entry_search_id.get().strip()
        result = search.search_student(search_id)  # Call the search method

        # Debugging print to see the result of the search
        print(f"Search result: {result}")  # This will show the result from the search function

        # Clear previous search result labels in content_frame
        for widget in content_frame.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.destroy()

        # Check if the result is a valid student (assuming search returns a list or tuple)
        if result and isinstance(result, list):  # Assuming the search returns a list with student data
            # Debugging message
            print(f"Student found: {result}")

            # Display student's information
            ttk.Label(content_frame, text="Student Found", style="Content.TLabel", font=("Arial", 28, "bold")).pack(pady=30)
            ttk.Label(content_frame, text=f"Name: {result[0]}", style="Content.TLabel").pack(pady=10)
            ttk.Label(content_frame, text=f"Age: {result[1]}", style="Content.TLabel").pack(pady=10)
            ttk.Label(content_frame, text=f"Student ID: {result[2]}", style="Content.TLabel").pack(pady=10)
            ttk.Label(content_frame, text=f"Email: {result[3]}", style="Content.TLabel").pack(pady=10)
            ttk.Label(content_frame, text=f"Phone: {result[4]}", style="Content.TLabel").pack(pady=10)
        else:
            # Debugging message
            print("No student found. Displaying error message.")
            
            # If no student is found, show an error message
            ttk.Label(content_frame, text="No student found with that ID.", font=("Arial", 16, "bold"), foreground="#d32f2f", background="#fce4ec").pack(pady=10)

        # Recreate the design label
        design = ttk.Label(content_frame, text="･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f")
        design.pack(pady=10)


    # Button to trigger the search
    ttk.Button(search_frame, text="Search", command=search_and_display, style="Login.TButton").pack(pady=20)


# Login function
attempts = 0  # Initialize attempts counter

# Login function
attempts = 0  # Initialize attempts counter

def login(idnum):
    global attempts  # Use the global attempts variable

    if attempts >= 3:
        lblError.config(text="You have exceeded the number of attempts. Goodbye.")
        win.after(1000, win.quit)
        return

    student = search.verify_login(idnum)
    if student:
        login_frame.place_forget()
        main_frame.pack(fill="both", expand=True)
        
        # Display welcome message with student name
        ttk.Label(content_frame, text=f"Welcome, {student[0]}", style="Content.TLabel", font=("Arial", 28, "bold")).pack(pady=30)
        
        # Display "Merry Christmas" message
        ttk.Label(content_frame, text="Merry Christmas!", style="Content.TLabel", font=("Arial", 28, "bold"), foreground="#880e4f").pack(pady=10)
        
        # Display the lyrics to "It's Beginning to Look a Lot Like Christmas"
        lyrics = "It's beginning to look a lot like Christmas,\nEverywhere you go!"
        ttk.Label(content_frame, text=lyrics, style="Content.TLabel", font=("Arial", 24), foreground="#880e4f").pack(pady=20)
        
        # Add some Christmas-themed decorations
        christmas_design = ttk.Label(content_frame, text="･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f")
        christmas_design.pack(pady=10)

        # Call the navbar function after displaying messages
        create_navbar(idnum)  # Pass idnum to create_navbar
    else:
        attempts += 1
        lblError.config(text=f"Invalid Login Credentials. Attempt {attempts} of 3.")


# Function to register a new student
def register_student():
    # Create the registration form frame
    register_frame = ttk.Frame(content_frame, style="Content.TFrame")
    register_frame.pack(pady=30)

    # Labels and Entries for each student detail
    ttk.Label(register_frame, text="Enter Student Name:", style="Content.TLabel").pack(pady=10)
    entry_name = ttk.Entry(register_frame, style="Login.TEntry", font=("Arial", 16), width=30)
    entry_name.pack(pady=10)

    ttk.Label(register_frame, text="Enter Student Age:", style="Content.TLabel").pack(pady=10)
    entry_age = ttk.Entry(register_frame, style="Login.TEntry", font=("Arial", 16), width=30)
    entry_age.pack(pady=10)

    ttk.Label(register_frame, text="Enter Student ID:", style="Content.TLabel").pack(pady=10)
    entry_id = ttk.Entry(register_frame, style="Login.TEntry", font=("Arial", 16), width=30)
    entry_id.pack(pady=10)

    ttk.Label(register_frame, text="Enter Student Email:", style="Content.TLabel").pack(pady=10)
    entry_email = ttk.Entry(register_frame, style="Login.TEntry", font=("Arial", 16), width=30)
    entry_email.pack(pady=10)

    ttk.Label(register_frame, text="Enter Student Phone:", style="Content.TLabel").pack(pady=10)
    entry_phone = ttk.Entry(register_frame, style="Login.TEntry", font=("Arial", 16), width=30)
    entry_phone.pack(pady=10)

    # Function to handle the registration process
    def handle_registration():
        name = entry_name.get().strip()
        age = entry_age.get().strip()
        idnum = entry_id.get().strip()
        email = entry_email.get().strip()
        phone = entry_phone.get().strip()

        # Simple validation for empty fields
        if not name or not age or not idnum or not email or not phone:
            ttk.Label(register_frame, text="All fields must be filled out!", style="Content.TLabelError").pack(pady=10)
        else:
            # Add student using the AddStudent class
            addstud.add(name, age, idnum, email, phone)

            # Inform the user that the student was added successfully
            ttk.Label(register_frame, text="Student Registered Successfully!", style="Content.TLabel", font=("Arial", 16, "bold")).pack(pady=20)

            # Optionally clear the form or hide it after registration
            # For this example, we just clear the inputs
            entry_name.delete(0, 'end')
            entry_age.delete(0, 'end')
            entry_id.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_phone.delete(0, 'end')

    # Button to register the student
    ttk.Button(register_frame, text="Register Student", command=handle_registration, style="Login.TButton").pack(pady=20)


# Function to display all students in a table format
# Function to display all students in a table format with pink theme and larger text
def view_all_students():
    # Clear the content frame to remove existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create a label for "View All Students" section
    ttk.Label(content_frame, text="All Students Information", style="Content.TLabel", font=("Arial", 32, "bold"), foreground="#880e4f").pack(pady=30)

    # Create a frame to hold the grid layout and center it
    grid_frame = ttk.Frame(content_frame)
    grid_frame.pack(pady=20, fill="both", expand=True)

    # Center the grid content (expand the grid to take full space)
    grid_frame.grid_columnconfigure(0, weight=1, uniform="equal")
    grid_frame.grid_columnconfigure(1, weight=1, uniform="equal")
    grid_frame.grid_columnconfigure(2, weight=1, uniform="equal")
    grid_frame.grid_columnconfigure(3, weight=1, uniform="equal")
    grid_frame.grid_columnconfigure(4, weight=1, uniform="equal")

    # Create headers for the grid (centered)
    headers = ["Name", "Age", "ID", "Email", "Phone"]
    for col, header in enumerate(headers):
        header_label = ttk.Label(grid_frame, text=header, style="Content.TLabel", font=("Arial", 18, "bold"), anchor="center")
        header_label.grid(row=0, column=col, padx=20, pady=10, sticky="ew")

    # Populate the grid with student data (centered)
    for row, student in enumerate(stu.allstudents, start=1):
        for col, value in enumerate(student):
            value_label = ttk.Label(grid_frame, text=value, style="Content.TLabel", font=("Arial", 16), anchor="center")
            value_label.grid(row=row, column=col, padx=20, pady=10, sticky="ew")

    # Optional decorative label at the bottom
    design = ttk.Label(content_frame, text="･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆", style="Content.TLabel", font=("Arial", 16, "bold"), foreground="#880e4f")
    design.pack(pady=10)


# Start the tkinter main loop
win.mainloop()
