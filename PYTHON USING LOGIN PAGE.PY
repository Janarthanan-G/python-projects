import tkinter as tk

# Function to change the content based on navigation
def show_content(content_frame, content):
    # Clear the previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    if content == "Home":
        tk.Label(content_frame, text="Welcome to My Portfolio!", font=("Arial", 18), pady=10).pack()
        tk.Label(content_frame, text="I'm a Junior Data Analysis and UI design Developer.", font=("Arial", 14), pady=5).pack()
    elif content == "About Me":
        tk.Label(content_frame, text="About Me", font=("Arial", 18), pady=10).pack()
        about_text = (
            "Hi, I'm Janarthanan. I specialize in UI design for smart home applications and automation.\n"
            "Currently, I'm interning in a data science role at Besant Technology and have a background in UI design."
        )
        tk.Label(content_frame, text=about_text, font=("Arial", 12), pady=10, justify="left").pack()
    elif content == "Projects":
        tk.Label(content_frame, text="My Projects", font=("Arial", 18), pady=10).pack()
        project_text = (
            "1. Impact of Covid19 IT companies in India\n"
            "   To collect the data from Google for random data to done the project\n"  
            "2. Mycamu for student registration to apply the companies and get conformation of mail\n"
            "   The project is done by the Tkinter connect the MySql,and E-mail\n"   
            "3. Smart Home UI Design (Figma)\n"
            "   Developed intuitive interfaces for smart home control applications.\n"
            "4. Automation Scripts (Python)\n"
            "   Created scripts for automating smart home devices.\n"
            "5. Data Analysis Project (Python)\n"
            "   Conducted data analysis and visualizations during my internship."
        )
        tk.Label(content_frame, text=project_text, font=("Arial", 12), pady=10, justify="left").pack()
    elif content == "Contact":
        tk.Label(content_frame, text="Contact Me", font=("Arial", 18), pady=10).pack()
        contact_text = "Email: janarthanangvbj123@gmail.com\nLinkedIn: www.linkedin.com/in/janarthanan01"
        tk.Label(content_frame, text=contact_text, font=("Arial", 12), pady=10).pack()

# Main function to create the portfolio window
def create_window():
    window = tk.Tk()
    window.title("Portfolio")
    window.geometry("600x400")

    # Header Section
    header = tk.Frame(window, bg="blue", height=50)
    header.pack(fill="x")
    header_label = tk.Label(header, text="My Portfolio", fg="white", bg="blue", font=("Arial", 20))
    header_label.pack(pady=10)

    # Navigation Bar Section
    nav_bar = tk.Frame(window, bg="gray", height=30)
    nav_bar.pack(fill="x")
    
    # Create buttons for navigation
    home_button = tk.Button(nav_bar, text="Home", command=lambda: show_content(content_frame, "Home"))
    about_button = tk.Button(nav_bar, text="About Me", command=lambda: show_content(content_frame, "About Me"))
    projects_button = tk.Button(nav_bar, text="Projects", command=lambda: show_content(content_frame, "Projects"))
    contact_button = tk.Button(nav_bar, text="Contact", command=lambda: show_content(content_frame, "Contact"))
    
    home_button.pack(side="left", padx=10, pady=5)
    about_button.pack(side="left", padx=10, pady=5)
    projects_button.pack(side="left", padx=10, pady=5)
    contact_button.pack(side="left", padx=10, pady=5)

    # Content Section
    content_frame = tk.Frame(window, bg="white")
    content_frame.pack(fill="both", expand=True, pady=20, padx=20)

    # Footer Section
    footer = tk.Frame(window, bg="blue", height=30)
    footer.pack(fill="x", side="bottom")
    footer_label = tk.Label(footer, text="© 2024 My Portfolio", fg="white", bg="blue")
    footer_label.pack(pady=5)

    # Load the initial home content
    show_content(content_frame, "Home")

    window.mainloop()

if __name__ == "__main__":
    create_window()
