import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL database connection
def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",  # Change this to your DB host
            user="root",       # Change to your DB user
            password="password",  # Change to your DB password
            database="registration_db"  # Change to your DB name
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None

# Function to handle signup
def signup():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Simple validation
    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        messagebox.showinfo("Success", "You have signed up successfully!")

        # Optionally, you can store the data somewhere, such as in a file or database
        with open("user_data.txt", "a") as file:
            file.write(f"Username: {username}, Email: {email}, Password: {password}\n")

        # Clear the form
        entry_username.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_confirm_password.delete(0, tk.END)

        # Open the registration form after signup
        open_registration_form()

# Function to handle form submission and store in MySQL
def submit_form():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        
        # Get input values
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        age = spin_age.get()
        email = entry_email_reg.get()
        college_name = entry_college.get()
        department = entry_department.get()
        passed_year = spin_passed_year.get()
        cgpa = entry_cgpa.get()
        skills = entry_skills.get()
        achievements = entry_achievements.get("1.0", tk.END).strip()
        projects = entry_projects.get("1.0", tk.END).strip()

        # Insert data into MySQL
        try:
            query = """INSERT INTO registrations (first_name, last_name, age, email, college_name, department, 
                                                  passed_year, cgpa, skills, achievements, projects) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (first_name, last_name, age, email, college_name, department, passed_year, cgpa, skills, achievements, projects))
            conn.commit()
            messagebox.showinfo("Success", "Form submitted and stored in database successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error inserting data: {err}")
        finally:
            cursor.close()
            conn.close()

# Function to open registration form
def open_registration_form():
    signup_window.withdraw()  # Hide signup window

    # Create registration window
    global registration_window
    registration_window = tk.Toplevel()
    registration_window.title("Registration Form")
    registration_window.geometry("500x600")

    # Create a frame to center the form
    form_frame = tk.Frame(registration_window, bg="#ffffff", bd=2, relief=tk.SOLID)
    form_frame.pack(pady=20, padx=20)

    # Labels and input fields for personal information
    tk.Label(form_frame, text="First Name:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, pady=5, sticky="e")
    global entry_first_name
    entry_first_name = tk.Entry(form_frame, font=("Arial", 12))
    entry_first_name.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Last Name:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, pady=5, sticky="e")
    global entry_last_name
    entry_last_name = tk.Entry(form_frame, font=("Arial", 12))
    entry_last_name.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Age:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, pady=5, sticky="e")
    global spin_age
    spin_age = tk.Spinbox(form_frame, from_=18, to=60, font=("Arial", 12))
    spin_age.grid(row=2, column=1, pady=5)

    tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, pady=5, sticky="e")
    global entry_email_reg
    entry_email_reg = tk.Entry(form_frame, font=("Arial", 12))
    entry_email_reg.grid(row=3, column=1, pady=5)

    tk.Label(form_frame, text="College Name:", font=("Arial", 12), bg="#ffffff").grid(row=4, column=0, pady=5, sticky="e")
    global entry_college
    entry_college = tk.Entry(form_frame, font=("Arial", 12))
    entry_college.grid(row=4, column=1, pady=5)

    tk.Label(form_frame, text="Department:", font=("Arial", 12), bg="#ffffff").grid(row=5, column=0, pady=5, sticky="e")
    global entry_department
    entry_department = tk.Entry(form_frame, font=("Arial", 12))
    entry_department.grid(row=5, column=1, pady=5)

    tk.Label(form_frame, text="Passed Out Year:", font=("Arial", 12), bg="#ffffff").grid(row=6, column=0, pady=5, sticky="e")
    global spin_passed_year
    spin_passed_year = tk.Spinbox(form_frame, from_=2000, to=2024, font=("Arial", 12))
    spin_passed_year.grid(row=6, column=1, pady=5)

    tk.Label(form_frame, text="CGPA:", font=("Arial", 12), bg="#ffffff").grid(row=7, column=0, pady=5, sticky="e")
    global entry_cgpa
    entry_cgpa = tk.Entry(form_frame, font=("Arial", 12))
    entry_cgpa.grid(row=7, column=1, pady=5)

    tk.Label(form_frame, text="Skills:", font=("Arial", 12), bg="#ffffff").grid(row=8, column=0, pady=5, sticky="e")
    global entry_skills
    entry_skills = tk.Entry(form_frame, font=("Arial", 12))
    entry_skills.grid(row=8, column=1, pady=5)

    tk.Label(form_frame, text="Achievements:", font=("Arial", 12), bg="#ffffff").grid(row=9, column=0, pady=5, sticky="e")
    global entry_achievements
    entry_achievements = tk.Text(form_frame, height=3, width=25, font=("Arial", 12))
    entry_achievements.grid(row=9, column=1, pady=5)

    tk.Label(form_frame, text="Projects:", font=("Arial", 12), bg="#ffffff").grid(row=10, column=0, pady=5, sticky="e")
    global entry_projects
    entry_projects = tk.Text(form_frame, height=3, width=25, font=("Arial", 12))
    entry_projects.grid(row=10, column=1, pady=5)

    # Submit button
    submit_button = tk.Button(form_frame, text="Submit", command=submit_form, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), bd=0)
    submit_button.grid(row=11, column=0, columnspan=2, pady=20)

# Create the signup window
signup_window = tk.Tk()
signup_window.title("Signup Form")

# Set the size of the window to a fixed size and center it on the screen
window_width = 400
window_height = 400
screen_width = signup_window.winfo_screenwidth()
screen_height = signup_window.winfo_screenheight()

x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

signup_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Set background color for the window
signup_window.configure(bg="#f0f0f0")  # light grey background

# Create a frame for the form to center it
form_frame = tk.Frame(signup_window, bg="#ffffff", bd=2, relief=tk.SOLID)
form_frame.pack(pady=20, padx=20)

# Create labels and entry widgets for signup
label_title = tk.Label(form_frame, text="Signup Form", font=("Arial", 16, "bold"), bg="#ffffff")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_username = tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#ffffff")
label_username.grid(row=1, column=0, pady=5, sticky='e')
entry_username = tk.Entry(form_frame, font=("Arial", 12))
entry_username.grid(row=1, column=1, pady=5)

label_email = tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#ffffff")
label_email.grid(row=2, column=0, pady=5, sticky='e')
entry_email = tk.Entry(form_frame, font=("Arial", 12))
entry_email.grid(row=2, column=1, pady=5)

label_password = tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#ffffff")
label_password.grid(row=3, column=0, pady=5, sticky='e')
entry_password = tk.Entry(form_frame, font=("Arial", 12), show="*")
entry_password.grid(row=3, column=1, pady=5)

label_confirm_password = tk.Label(form_frame, text="Confirm Password:", font=("Arial", 12), bg="#ffffff")
label_confirm_password.grid(row=4, column=0, pady=5, sticky='e')
entry_confirm_password = tk.Entry(form_frame, font=("Arial", 12), show="*")
entry_confirm_password.grid(row=4, column=1, pady=5)

# Create signup button
button_signup = tk.Button(form_frame, text="Sign Up", command=signup, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), bd=0)
button_signup.grid(row=5, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
signup_window.mainloop()
