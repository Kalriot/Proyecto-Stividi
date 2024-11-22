import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        
        # Lista de tareas
        self.tasks = []

        # Widgets principales
        self.title_label = tk.Label(self.root, text="Task Manager", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", font=("Helvetica", 12), command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 14), height=15, width=30, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", font=("Helvetica", 12), command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", font=("Helvetica", 12), command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def clear_tasks(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirm:
            self.tasks.clear()
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
