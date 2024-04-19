import tkinter as tk
from tkinter import messagebox

# Function to increase the point
def increase_score():
    global score
    score += 1

# Function to display next question
def display_question():
    global question_label, option_buttons, current_question
    clear_widgets()

    if current_question < len(questions):
        question_label = tk.Label(root, text=questions[current_question], font=("Arial", 24, "bold"), wraplength=600, justify="center")
        question_label.place(relx=0.5, rely=0.2, anchor="center")

        option_buttons = []
        for idx, option in enumerate(options[current_question]):
            button = tk.Button(root, text=option, font=("Arial", 18), width=30, bg="#4CAF50", fg="white", command=lambda idx=idx: option_click(idx))
            button.place(relx=0.5, rely=0.4 + idx * 0.1, anchor="center")
            option_buttons.append(button)
    else:
        show_score()

# Function to handle option click
def option_click(index):
    global current_question
    if index == correct_answers[current_question]:
        increase_score()
    current_question += 1
    display_question()

# Function to clear widgets
def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# Function to start the quiz
def start_quiz():
    clear_widgets()
    global score, current_question
    score = 0
    current_question = 0
    display_question()

# Function to show final score
def show_score():
    clear_widgets()
    tk.Label(root, text="Your Score", font=("Arial", 30)).pack(pady=20)
    tk.Label(root, text=f"{score}/{len(questions)}", font=("Arial", 25)).pack(pady=20)
    tk.Button(root, text="Restart", font=("Arial", 20), command=start_quiz).pack(pady=20)

# Function to register
def register():
    global username_entry, password_entry
    clear_widgets()
    tk.Label(root, text="Register", font=("Arial", 30)).pack(pady=20)
    tk.Label(root, text="Username:", font=("Arial", 20)).pack(pady=10)
    username_entry = tk.Entry(root, font=("Arial", 20))
    username_entry.pack(pady=5)
    tk.Label(root, text="Password:", font=("Arial", 20)).pack(pady=10)
    password_entry = tk.Entry(root, font=("Arial", 20), show="*")
    password_entry.pack(pady=5)
    tk.Button(root, text="Register", font=("Arial", 20), command=register_user).pack(pady=20)
    tk.Button(root, text="Back", font=("Arial", 20), command=home_page).pack(pady=20)

# Function to handle registration
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("Success", "Registration Successful!")
    else:
        messagebox.showerror("Error", "Username and Password are required.")

# Function to login
def login():
    global username_entry, password_entry
    clear_widgets()
    tk.Label(root, text="Login", font=("Arial", 30)).pack(pady=20)
    tk.Label(root, text="Username:", font=("Arial", 20)).pack(pady=10)
    username_entry = tk.Entry(root, font=("Arial", 20))
    username_entry.pack(pady=5)
    tk.Label(root, text="Password:", font=("Arial", 20)).pack(pady=10)
    password_entry = tk.Entry(root, font=("Arial", 20), show="*")
    password_entry.pack(pady=5)
    tk.Button(root, text="Login", font=("Arial", 20), command=start_quiz).pack(pady=20)
    tk.Button(root, text="Back", font=("Arial", 20), command=home_page).pack(pady=20)

# Function to go back to home page
def home_page():
    clear_widgets()
    tk.Button(root, text="Register", font=("Arial", 20), command=register).pack(pady=20)
    tk.Button(root, text="Login", font=("Arial", 20), command=login).pack(pady=20)

# Main tkinter window
root = tk.Tk()
root.title("QUIZ")
root.geometry('800x600')

# Quiz data
questions = [
    "Which of them is a Keyword in Python?",
    "Which of the following is a built-in function in Python?",
    "Which of the following is not the core datatype in Python?",
    "Who developed python programming language?",
    "Which of the following is the extension for Python File?",
    "What is the output of '2' + '3' in Python?",
    "What does the 'append()' method do in Python?",
    "What is the result of 2**3 in Python?",
    "What is the output of 'Python'[1:]?",
    "What is the purpose of the 'if' statement in Python?"
]

options = [
    ["range", "def", "Val", "to"],
    ["factorial()", "print()", "seed()", "sqrt()"],
    ["Tuple", "Dictionary", "Lists", "Class"],
    ["Wick Van Rossum", "Rasmus Lerdorf", "Guido Van Rossum", "Niene Stom"],
    [".python", ".p", ".pl", ".py"],
    ["5", "'23'", "TypeError", "'2'+'3'"],
    ["Adds a new item to the end of a list", "Removes the last item from a list", "Sorts the list", "Returns the index of the specified item"],
    ["5", "8", "6", "23"],
    ["Python", "P", "ytho", "ython"],
    ["To execute code only if a certain condition is true", "To loop through items in a sequence", "To define a function", "To handle exceptions"]
]

correct_answers = [1, 1, 3, 2, 3, 1, 0, 1, 3, 0]  # Index of correct option for each question

score = 0
current_question = 0

# Home page buttons
tk.Button(root, text="Register", font=("Arial", 20), command=register).pack(pady=20)
tk.Button(root, text="Login", font=("Arial", 20), command=login).pack(pady=20)

root.mainloop()
