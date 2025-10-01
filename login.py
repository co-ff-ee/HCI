import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, Admin!")
        root.destroy()
        subprocess.run([sys.executable, "personal_info.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def reset_login():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def cancel_login():
    root.destroy()

# ---------------- DARK THEME COLORS ----------------
bg_color = "#1e1e1e"   # dark gray
fg_color = "#ffffff"   # white text
btn_bg = "#333333"     # dark button
btn_fg = "#ffffff"

# Main Window
root = tk.Tk()
root.title("Login Window")
root.geometry("400x250")
root.configure(bg=bg_color)

tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg=bg_color, fg=fg_color).pack(pady=10)

frame_login = tk.Frame(root, bg=bg_color)
frame_login.pack(pady=10)

# Username
tk.Label(frame_login, text="Username:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username = tk.Entry(frame_login, bg="#2b2b2b", fg=fg_color, insertbackground="white")
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password
tk.Label(frame_login, text="Password:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password = tk.Entry(frame_login, show="*", bg="#2b2b2b", fg=fg_color, insertbackground="white")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg=bg_color)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Login", width=10, command=login, bg=btn_bg, fg=btn_fg).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset", width=10, command=reset_login, bg=btn_bg, fg=btn_fg).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Cancel", width=10, command=cancel_login, bg=btn_bg, fg=btn_fg).grid(row=0, column=2, padx=5)

root.mainloop()
