import tkinter as tk
from tkinter import messagebox, filedialog
import re
import smtplib

# Dummy data storage (replace this with actual database code if needed)
users = {}

# Function to send confirmation email
def send_confirmation_email(user_email):
    try:
        sender_email = "youremail@example.com"  # Replace with your email
        sender_password = "yourpassword"  # Replace with your email password

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            subject = "Login Confirmation"
            body = f"Hello, {user_email}. You have successfully logged in."
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender_email, user_email, message)

        messagebox.showinfo("Success", "Confirmation email sent!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# Function to validate inputs
def validate_inputs(email, password, phone):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    phone_pattern = r'^\d{10}$'  # Phone number must be 10 digits

    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "Invalid email format")
        return False
    if len(password) < 8:
        messagebox.showerror("Error", "Password should be at least 8 characters long")
        return False
    if phone and not re.match(phone_pattern, phone):
        messagebox.showerror("Error", "Phone number should be 10 digits")
        return False

    return True

# Sign-in page functionality
def register_user():
    email = email_entry.get()
    password = password_entry.get()

    if validate_inputs(email, password, ''):
        users[email] = password
        messagebox.showinfo("Success", "Account created successfully!")
    else:
        messagebox.showerror("Error", "Invalid input, please try again.")

# Login page functionality
def login_user():
    email = login_email_entry.get()
    password = login_password_entry.get()

    if email in users and users[email] == password:
        messagebox.showinfo("Success", "Login successful!")
        send_confirmation_email(email)  # Send confirmation email after successful login
        employee_details_gui()  # Move to employee details page
    else:
        messagebox.showerror("Error", "Incorrect email or password")

# Employee details page GUI
def employee_details_gui():
    details_window = tk.Tk()
    details_window.title("Employee Details")

    tk.Label(details_window, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(details_window)
    name_entry.grid(row=0, column=1)

    tk.Label(details_window, text="Age").grid(row=1, column=0)
    age_entry = tk.Entry(details_window)
    age_entry.grid(row=1, column=1)

    tk.Label(details_window, text="Date of Birth").grid(row=2, column=0)
    dob_entry = tk.Entry(details_window)
    dob_entry.grid(row=2, column=1)

    tk.Label(details_window, text="Email ID").grid(row=3, column=0)
    email_entry = tk.Entry(details_window)
    email_entry.grid(row=3, column=1)

    tk.Label(details_window, text="Current Company").grid(row=4, column=0)
    company_entry = tk.Entry(details_window)
    company_entry.grid(row=4, column=1)

    tk.Label(details_window, text="Position").grid(row=5, column=0)
    position_entry = tk.Entry(details_window)
    position_entry.grid(row=5, column=1)

    tk.Label(details_window, text="Title of Projects").grid(row=6, column=0)
    project_entry = tk.Entry(details_window)
    project_entry.grid(row=6, column=1)

    tk.Label(details_window, text="Previous Company Details").grid(row=7, column=0)
    previous_company_entry = tk.Entry(details_window)
    previous_company_entry.grid(row=7, column=1)

    # Photo Upload
    def upload_photo():
        file_path = filedialog.askopenfilename()
        messagebox.showinfo("Photo Upload", f"Photo uploaded: {file_path}")

    tk.Button(details_window, text="Upload Photo", command=upload_photo).grid(row=8, column=1)

    tk.Button(details_window, text="Submit", command=lambda: messagebox.showinfo("Success", "Details saved successfully!")).grid(row=9, column=1)

    details_window.mainloop()

# GUI for Sign-in Page
root = tk.Tk()
root.title("Sign-In Page")

tk.Label(root, text="Email").grid(row=0, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Button(root, text="Sign In", command=register_user).grid(row=2, column=1)

# GUI for Login Page
def login_gui():
    login_window = tk.Tk()
    login_window.title("Login Page")

    tk.Label(login_window, text="Email").grid(row=0, column=0)
    global login_email_entry
    login_email_entry = tk.Entry(login_window)
    login_email_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Password").grid(row=1, column=0)
    global login_password_entry
    login_password_entry = tk.Entry(login_window, show="*")
    login_password_entry.grid(row=1, column=1)

    tk.Button(login_window, text="Login", command=login_user).grid(row=2, column=1)

    login_window.mainloop()

# Call the login page
tk.Button(root, text="Go to Login", command=login_gui).grid(row=3, column=1)

root.mainloop()
