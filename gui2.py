import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Theme
        self.style = ttk.Style("darkly")  # Try "solar", "cyborg", or "morph"

        # Header
        ttk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bootstyle="primary").pack(pady=10)

        # Task Entry
        self.task_entry = ttk.Entry(root, font=("Helvetica", 12), width=30)
        self.task_entry.pack(pady=5)

        # Buttons
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=5)

        ttk.Button(btn_frame, text="Add Task", command=self.add_task, bootstyle="success").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Remove Task", command=self.remove_task, bootstyle="danger").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear All", command=self.clear_tasks, bootstyle="warning").pack(side=tk.LEFT, padx=5)

        # Task List
        self.task_list = tk.Listbox(root, font=("Helvetica", 12), width=40, height=12, bg="#f8f9fa", fg="black")
        self.task_list.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_task = self.task_list.curselection()
            self.task_list.delete(selected_task)
        except:
            messagebox.showwarning("Warning", "Please select a task to remove!")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)

# Run the App
if __name__ == "__main__":
    root = ttk.Window(themename="solar")  # Change theme here
    app = ToDoApp(root)
    root.mainloop()
