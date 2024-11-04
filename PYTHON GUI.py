import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Create the main window
GVBJ = Tk()
GVBJ.title("My App")
GVBJ.geometry("1440x1024")

GVBJ.config(bg="#002b80")

# Frame for positioning elements
frame = Frame(GVBJ)
frame.place(x=700, y=300)
frame.config(bg="#002b80")

# Welcome messages
Label(frame, text='Welcome to Creative Studio', font=('Georgia', 22),fg="white",bg="#002b80").grid(row=20, column=27, padx=10, pady=10 )
Label(frame, text='Janarthanan G', font=('Arial', 18),fg="white",bg="#002b80").grid(row=21, column=27, padx=10, pady=10)
Label(frame, text='This is my official portfolio website to show all details and work explains', font=('Arial', 15),fg="white",bg="#002b80").grid(row=22, column=27, padx=10, pady=10)

# Load and display the image

image = Image.open("C:/Users/Dell/Desktop/PYTHON DAILY TASK/PYTHONADV.PY/JANA.jpg")
image = image.resize((500, 800))  # Resize the image to fit
img = ImageTk.PhotoImage(image)
image_label = tk.Label(GVBJ, image=img)
image_label.grid(row=0, column=0)


#Home page dashboard 
menu = Menu(GVBJ)
GVBJ.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Home', menu=filemenu)
filemenu.add_command(label='About')
filemenu.add_command(label='Project')
filemenu.add_command(label='Skills')
filemenu.add_command(label='Googleform')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=GVBJ.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Contact')


def on_enter(event, button):
    button['bg'] = '#3498DB'

def on_leave(event, button):
    button['bg'] = '#2C3E50'

def display_content(content):
    # Clear previous content
    for widget in frame.winfo_children():
        widget.destroy()

    if content == "About":
        Label(frame, text="About", font=('Arial', 20), fg="white", bg="#002b80", pady=10).pack()
        Label(frame, text="Janarthanan G\nUI Designer and Developer", font=('Arial', 14), fg="white", bg="#002b80").pack(pady=10)
    elif content == "Project":
        Label(frame, text="Projects", font=('Arial', 20), fg="white", bg="#002b80", pady=10).pack()
        Label(frame, text="Project 1: Smart Home UI\nProject 2: Automation Scripts", font=('Arial', 14), fg="white", bg="#002b80").pack(pady=10)
    elif content == "Skills":
        Label(frame, text="Skills", font=('Arial', 20), fg="white", bg="#002b80", pady=10).pack()
        Label(frame, text="Figma, Python, Data Science", font=('Arial', 14), fg="white", bg="#002b80").pack(pady=10)
    elif content == "Googleform":
        Label(frame, text="Google Form", font=('Arial', 20), fg="white", bg="#002b80", pady=10).pack()
        Label(frame, text="Link: Google Form to fill details", font=('Arial', 14), fg="white", bg="#002b80").pack(pady=10)
    elif content == "Contact":
        Label(frame, text="Contact", font=('Arial', 20), fg="white", bg="#002b80", pady=10).pack()
        Label(frame, text="Email: youremail@example.com", font=('Arial', 14), fg="white", bg="#002b80").pack(pady=10)

for index, (label, command) in enumerate(()):
    btn = Button(menu, text=label, command=command**Button)
    btn.pack(pady=10)

    btn.bind("<Enter>", lambda event, b=btn: on_enter(event, b))
    btn.bind("<Leave>", lambda event, b=btn: on_leave(event, b))


Button = {
    "About": lambda: display_content("About"),
    "Project": lambda: display_content("Project"),
    "Skills": lambda: display_content("Skills"),
    "Googleform": lambda: display_content("Googleform"),
    "Contact": lambda: display_content("Contact"),
    "Exit": GVBJ.quit
}

# Styling for the menu buttons
Button_style = {
    "font": ('Arial', 14),
    "bg": "#2C3E50",
    "fg": "white",
    "activebackground": "#2980B9",
    "activeforeground": "white",
    "bd": 0,
    "relief": FLAT,
    "width": 20,
    "height": 2
}




# Start the main loop
GVBJ.mainloop()

