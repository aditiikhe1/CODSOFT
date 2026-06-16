import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.resizable(False, False)

# Functions
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    task_listbox.insert(tk.END, "❌ " + task)
    task_entry.delete(0, tk.END)


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")


def mark_complete():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if task.startswith("✅"):
            messagebox.showinfo("Info", "Task already completed!")
            return

        task = task.replace("❌ ", "")
        task_listbox.delete(selected)
        task_listbox.insert(selected, "✅ " + task)

    except:
        messagebox.showwarning("Warning", "Please select a task!")


def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        task_listbox.delete(0, tk.END)


# Title
title_label = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

# Entry Field
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=10)

# Add Button
add_button = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_button.pack(pady=5)

# Task List
task_listbox = tk.Listbox(
    root,
    width=50,
    height=15,
    font=("Arial", 12),
    selectbackground="lightblue"
)
task_listbox.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

complete_button = tk.Button(
    button_frame,
    text="Mark Complete",
    width=15,
    command=mark_complete
)
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=15,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    width=15,
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=5)

# Run Application
root.mainloop()