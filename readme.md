A simple command-line To-Do List application built using Python.
It allows users to add, view, and delete tasks, with all tasks saved in a text file so they remain available the next time you run the program.

🚀 Features

✔ View all tasks

✔ Add new tasks

✔ Delete tasks by number

✔ Automatically saves tasks in tasks.txt

✔ Loads saved tasks on startup

✔ Clean menu-based interface

📂 Project Structure
├── to_do_list.py      # Main Python program
└── tasks.txt          # File where tasks are stored (auto-created)

🛠 Requirements

Python 3.x

No external libraries required (uses only built-in modules)

▶️ How to Run

Download or copy the project files

Open a terminal or command prompt

Navigate to the project folder

Run the script:

python to_do_list.py


The program will start and show the menu.

📘 How It Works
1. Loading Tasks

When the program starts, it checks if tasks.txt exists and loads the tasks into a list.

2. Saving Tasks

Every time you add or delete a task, the updated list is stored back into the file.

3. Menu Options

1. View Tasks → Displays all existing tasks

2. Add Task → Allows you to enter a new task

3. Delete Task → Enter the task number to remove it

4. Exit → Exit the program

🧩 Code Example

Here is the main program entry point:

if __name__ == "__main__":
    main()


This ensures the program runs only when executed directly.

💡 Future Improvements

You can enhance the project by adding:

Marking tasks as completed

Task priorities (High/Medium/Low)

Due dates

A GUI version using Tkinter

Export tasks to CSV

Convert to an .exe file using PyInstaller

📜 License

This project is free to use for educational purposes.
