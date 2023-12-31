import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = []

        # Entry widget for task input
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for adding and removing tasks
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5)
        
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=0, column=2, padx=5)

        # Listbox to display the to-do list
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Button to quit the application
        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        quit_button.grid(row=2, column=0, columnspan=3, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.todo_list.pop(selected_index[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
