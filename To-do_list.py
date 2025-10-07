import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------- Database Connection ----------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ananya@1421",
        database="todo_db"
    )
    cursor = conn.cursor()
except mysql.connector.Error as e:
    messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
    exit()

# ---------- Create table if not exists ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL
)
""")
conn.commit()

# ---------- Functions ----------


def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT task FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row[0])


def add_task():
    task = entry.get().strip()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected[0])
        cursor.execute("DELETE FROM tasks WHERE task = %s", (task,))
        conn.commit()
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        load_tasks()


# ---------- UI Setup ----------
root = tk.Tk()
root.title("To-Do List App (MySQL)")
root.geometry("400x400")
root.config(bg="#E8EAF6")

tk.Label(root, text="My To-Do List", font=("Arial",
         18, "bold"), bg="#E8EAF6").pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.grid(row=0, column=0, padx=5)
tk.Button(frame, text="Add Task", command=add_task,
          bg="#7986CB", fg="white").grid(row=0, column=1)

listbox = tk.Listbox(root, width=45, height=10, font=("Arial", 12))
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Delete Task", command=delete_task,
          bg="#E57373", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear All", command=clear_all,
          bg="#BA68C8", fg="white").grid(row=0, column=1, padx=10)

load_tasks()

root.mainloop()
