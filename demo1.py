import tkinter as tk
from tkinter import messagebox
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

# MySQL Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janarthanan@1812",  # Replace with your MySQL password
    database="apply_for_job"
)
cursor = conn.cursor()

# Create the table for storing users if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50),
        email VARCHAR(100)
    )
''')
conn.commit()

# Create the table for storing job applications if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_applications (
        app_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        middle_name VARCHAR(50),
        last_name VARCHAR(50),
        dob DATE,
        age INT,
        email VARCHAR(100),
        mobile_number VARCHAR(15),
        degree_year INT,
        cgpa FLOAT,
        college_name VARCHAR(100),
        department VARCHAR(100),
        skills TEXT,
        projects TEXT,
        candidate_fit TEXT
    )
''')
conn.commit()





# Function to validate email and mobile patterns
def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email)

def validate_mobile(mobile):
    mobile_pattern = r'^[6-9]\d{9}$'  # Indian mobile pattern
    return re.match(mobile_pattern, mobile)

# Function to handle login
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
        open_job_application_form()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle registration
def register():
    registration_window = tk.Toplevel(root)
    registration_window.title("Register")
    registration_window.geometry("400x450")
    registration_window.config(bg="#f0f0f5")

    tk.Label(registration_window, text="Register", font=("Arial", 18, "bold"), bg="#f0f0f5", fg="#333").pack(pady=20)

    tk.Label(registration_window, text="Username:", font=("Arial", 12), bg="#f0f0f5").pack(pady=5)
    register_username_entry = tk.Entry(registration_window, font=("Arial", 12), bd=2)
    register_username_entry.pack(pady=5)

    tk.Label(registration_window, text="Password:", font=("Arial", 12), bg="#f0f0f5").pack(pady=5)
    register_password_entry = tk.Entry(registration_window, font=("Arial", 12), show="*", bd=2)
    register_password_entry.pack(pady=5)

    tk.Label(registration_window, text="Email:", font=("Arial", 12), bg="#f0f0f5").pack(pady=5)
    register_email_entry = tk.Entry(registration_window, font=("Arial", 12), bd=2)
    register_email_entry.pack(pady=5)

    def submit_registration():
        username = register_username_entry.get()
        password = register_password_entry.get()
        email = register_email_entry.get()

        # Check if fields are filled and patterns are correct
        if not (username and password and email):
            messagebox.showerror("Error", "All fields are required!")
            return

        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        # Check if username already exists
        try:
            query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password, email))
            conn.commit()
            messagebox.showinfo("Registration Successful", f"Account created for {username}!")
            registration_window.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Username already exists or other error: {err}")
        

       

    tk.Button(registration_window, text="Register", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
              command=submit_registration, width=15).pack(pady=20)

# Function to open job application form
def open_job_application_form():
    app_window = tk.Toplevel(root)
    app_window.title("Job Vacancy Form")
    app_window.geometry("700x500")
    app_window.config(bg="#e6f2ff")

    tk.Label(app_window, text="Job Vacancy Form", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#333").pack(pady=10)

    form_frame = tk.Frame(app_window, bg="#e6f2ff")
    form_frame.pack(pady=10)

    fields = [
        ("First Name *", "first_name"), 
        ("Middle Name", "middle_name"), 
        ("Last Name", "last_name"), 
        ("Date of Birth (YYYY-MM-DD)", "dob"), 
        ("Age", "age"), 
        ("Email *", "email"), 
        ("Mobile Number *", "mobile_number"), 
        ("Degree Passed Out Year *", "degree_year"), 
        ("Overall CGPA *", "cgpa"), 
        ("College Name", "college_name"), 
        ("Department of College", "department"), 
        ("Skills", "skills"), 
        ("Projects", "projects"), 
        ("Describe how the candidate fits the job", "candidate_fit")
    ]

    entries = {}
    for idx, (field_label, field_name) in enumerate(fields):
        tk.Label(form_frame, text=field_label, font=("Arial", 12), bg="#e6f2ff").grid(row=idx//2, column=(idx % 2) * 2, padx=10, pady=10)
        entry = tk.Entry(form_frame, font=("Arial", 12), bd=2)
        entry.grid(row=idx//2, column=(idx % 2) * 2 + 1, padx=10, pady=10)
        entries[field_name] = entry

    def submit_application():
        data = {field: entries[field].get() for _, field in fields}

        required_fields = ["first_name", "email", "mobile_number", "degree_year", "cgpa"]
        missing_fields = [field for field in required_fields if not data[field]]
        if missing_fields:
            messagebox.showerror("Error", "Please fill out the required fields: " + ", ".join(missing_fields))
            return

        if not validate_email(data["email"]):
            messagebox.showerror("Error", "Invalid email format!")
            return

        if not validate_mobile(data["mobile_number"]):
            messagebox.showerror("Error", "Invalid mobile number format!")
            return

        try:
            query = '''INSERT INTO job_applications 
                       (first_name, middle_name, last_name, dob, age, email, mobile_number, degree_year, 
                        cgpa, college_name, department, skills, projects, candidate_fit) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(query, tuple(data.values()))
            conn.commit()
            messagebox.showinfo("Application Submitted", "Job application submitted successfully!")
            
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error submitting job application: {err}")

        
        try:
                # Set up the server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Transport layer security

                    # Login credentials for sending the mail
            sender_email = 'janarthanann123@gmail.com'
            sender_password = 'syhm ooyk oaia pcuz'  # Use app password if 2FA is enabled

            server.login(sender_email, sender_password)

                    # Email content
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = data['email']
            message['Subject'] = 'Registration Successful'

                    # MIME text of the email
            body = f"Dear {data['first_name']},\n\nYour Job application form Registration was Successful!\n\nThank you for registering."
            message.attach(MIMEText(body, 'plain'))

                    # Send the email
            text = message.as_string()
            server.sendmail(sender_email,data['email'], text)

                    # Success message
            print("Email sent successfully!")
                
        except Exception as e:
            print(f"Error sending email: {str(e)}")

        finally:
                    # Disconnect from the server
            server.quit()    

    tk.Button(app_window, text="Submit Application", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
              command=submit_application, width=20).pack(pady=20)

# Main window
root = tk.Tk()
root.title("MyCamu Login")
root.geometry("400x350")
root.config(bg="#e6f2ff")

# Title
tk.Label(root, text="MyCamu Login", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#333").pack(pady=20)

# Login form
login_frame = tk.Frame(root, bg="#e6f2ff")
login_frame.pack(pady=10)

tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#e6f2ff").grid(row=0, column=0, padx=10, pady=10)
login_username_entry = tk.Entry(login_frame, font=("Arial", 12), bd=2)
login_username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#e6f2ff").grid(row=1, column=0, padx=10, pady=10)
login_password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*", bd=2)
login_password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login and Register buttons
tk.Button(root, text="Login", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
          command=login, width=15).pack(pady=10)
tk.Button(root, text="Register", font=("Arial", 12, "bold"), bg="#2196F3", fg="white",
          command=register, width=15).pack(pady=10)

root.mainloop()
