import tkinter as tk
from tkinter import ttk
import subprocess
import sys

def next_window():
    personal_window.destroy()
    # Run the next window (academic_info.py)
    subprocess.run([sys.executable, "academic_info.py"])

personal_window = tk.Tk()
personal_window.title("Personal Information")
personal_window.geometry("500x500")

tk.Label(personal_window, text="Personal Information", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(personal_window)
frame.pack(pady=10)

# Name
tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1)

# Address
tk.Label(frame, text="Address:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_address = tk.Entry(frame, width=30)
entry_address.grid(row=1, column=1)

# Contact Number
tk.Label(frame, text="Contact No:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_contact = tk.Entry(frame, width=30)
entry_contact.grid(row=2, column=1)

# Gender
tk.Label(frame, text="Gender:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female").grid(row=3, column=1, sticky="e")

# Blood Group
tk.Label(frame, text="Blood Group:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
blood_group_var = tk.StringVar()
combo_blood = ttk.Combobox(frame, textvariable=blood_group_var, values=blood_groups, state="readonly", width=27)
combo_blood.grid(row=4, column=1)

# Aadhaar Number
tk.Label(frame, text="Aadhaar No:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_aadhaar = tk.Entry(frame, width=30)
entry_aadhaar.grid(row=5, column=1)

# PAN Number
tk.Label(frame, text="PAN No:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
entry_pan = tk.Entry(frame, width=30)
entry_pan.grid(row=6, column=1)

# Next Button
btn_next = tk.Button(personal_window, text="Next", width=15, command=next_window)
btn_next.pack(pady=20)

personal_window.mainloop()
