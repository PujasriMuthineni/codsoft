from tkinter import *
from tkinter import messagebox, simpledialog
import sqlite3 as sql

class TaskDatabase:
    def __init__(self, db_name="listOfTasks.db"):
        self.conn = sql.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                title TEXT,
                completed INTEGER
            )
        """)

    def add_task(self, title):
        self.cursor.execute("INSERT INTO tasks VALUES (?, ?)", (title, 0))
        self.conn.commit()

    def update_task(self, old_title, new_title):
        self.cursor.execute("UPDATE tasks SET title = ? WHERE title = ?", (new_title, old_title))
        self.conn.commit()

    def mark_completed(self, title):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE title = ?", (title,))
        self.conn.commit()

    def delete_task(self, title):
        self.cursor.execute("DELETE FROM tasks WHERE title = ?", (title,))
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM tasks")
        self.conn.commit()

    def fetch_tasks(self):
        self.cursor.execute("SELECT title, completed FROM tasks")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class ToDoApp:
    def __init__(self, root):
        self.db = TaskDatabase()
        self.tasks = []

        root.title("To-Do List Application")
        root.geometry("700x450")
        root.resizable(False, False)
        root.config(bg="#D6F5E7")

        self.frame = Frame(root, bg="#8FDDE7")
        self.frame.pack(expand=True, fill="both")

        self.build_gui()


        self.load_tasks()

    
    def build_gui(self):
        Label(
            self.frame,
            text="TO-DO LIST\nEnter a New Task:",
            bg="#8FDDE7",
            fg="#FF6103",
            font=("Arial", 16, "bold")
        ).place(x=20, y=20)

       
        self.task_entry = Entry(self.frame, width=45, font=("Arial", 14))
        self.task_entry.place(x=220, y=38)

        Button(self.frame, text="Add Task", bg="#F4C20D", font=("Arial", 12, "bold"),
               command=self.add_task).place(x=50, y=90)

        Button(self.frame, text="Edit Task", bg="#F4C20D", font=("Arial", 12, "bold"),
               command=self.edit_task).place(x=180, y=90)

        Button(self.frame, text="Mark Completed", bg="#F4C20D", font=("Arial", 12, "bold"),
               command=self.mark_completed).place(x=310, y=90)

        Button(self.frame, text="Delete", bg="#F4C20D", font=("Arial", 12, "bold"),
               command=self.delete_task).place(x=470, y=90)

        Button(self.frame, text="Delete All", bg="#F4C20D", font=("Arial", 12, "bold"),
               command=self.delete_all).place(x=560, y=90)

        Button(self.frame, text="Exit", bg="#F4C20D", font=("Arial", 12, "bold"),
               command=self.exit_app).place(x=330, y=380)

        self.listbox = Listbox(
            self.frame, width=80, height=12,
            font=("Arial", 12),
            bg="white",
            selectbackground="#FFA07A"
        )
        self.listbox.place(x=20, y=150)


    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Error", "Task field is empty!")
            return

        self.db.add_task(task)
        self.load_tasks()
        self.task_entry.delete(0, "end")

    def edit_task(self):
        try:
            old_task = self.listbox.get(self.listbox.curselection())
            new_task = simpledialog.askstring("Edit Task", "Enter updated task:")
            if new_task:
                self.db.update_task(old_task.replace(" ✔ Done", ""), new_task)
                self.load_tasks()
        except:
            messagebox.showerror("Error", "No task selected!")

    def mark_completed(self):
        try:
            task = self.listbox.get(self.listbox.curselection())
            clean_task = task.replace(" ✔ Done", "")
            self.db.mark_completed(clean_task)
            self.load_tasks()
        except:
            messagebox.showwarning("Error", "No task selected!")

    def delete_task(self):
        try:
            task = self.listbox.get(self.listbox.curselection())
            self.db.delete_task(task.replace(" ✔ Done", ""))
            self.load_tasks()
        except:
            messagebox.showinfo("Error", "Please select a task to delete.")

    def delete_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.db.delete_all()
            self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, "end")
        tasks = self.db.fetch_tasks()

        for title, completed in tasks:
            if completed == 1:
                self.listbox.insert("end", f"{title} ✔ Done")
            else:
                self.listbox.insert("end", title)

    def exit_app(self):
        self.db.close()
        root.destroy()
if __name__ == "__main__":
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()


