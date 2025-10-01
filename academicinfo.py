import tkinter as tk
from tkinter import messagebox

academic_window = tk.Tk()
academic_window.title("Academic Information")
academic_window.geometry("500x600")

tk.Label(academic_window, text="Academic Information", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(academic_window)
frame.pack(pady=10)

# Academic fields
fields = ["10th Marks", "12th Marks", "1st Year Marks", "2nd Year Marks", 
          "Skills", "Certifications", "Strengths", "Weaknesses"]
entries = {}

for i, field in enumerate(fields):
    tk.Label(frame, text=f"{field}:").grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = tk.Entry(frame, width=30)
    entry.grid(row=i, column=1)
    entries[field] = entry

# Submit Button
def submit():
    data = {field: entry.get() for field, entry in entries.items()}
    messagebox.showinfo("Submission Success", f"Data Submitted:\n{data}")
    academic_window.destroy()

btn_submit = tk.Button(academic_window, text="Submit", width=15, command=submit)
btn_submit.pack(pady=20)

academic_window.mainloop()
