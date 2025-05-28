
import tkinter as tk
from tkinter import messagebox
import subprocess

def install_all():
    messagebox.showinfo("Installer", "Installing all KC HiperGrid modules...")
    subprocess.call(['bash', '../09_Installer_Scripts/install_macos.sh'])

def update_all():
    messagebox.showinfo("Updater", "Running updater...")
    subprocess.call(['bash', '../08_Automation/update_all.sh'])

def backup_system():
    messagebox.showinfo("Backup", "Creating backup...")
    subprocess.call(['bash', '../11_Backup_Recovery/macos_backup.sh'])

app = tk.Tk()
app.title("KC HiperGrid Installer")
app.geometry("400x300")

tk.Label(app, text="KC HiperGrid Cyber Defense System", font=("Helvetica", 14)).pack(pady=20)
tk.Button(app, text="Install All Tools", command=install_all, width=30).pack(pady=5)
tk.Button(app, text="Update Tools", command=update_all, width=30).pack(pady=5)
tk.Button(app, text="Create System Backup", command=backup_system, width=30).pack(pady=5)
tk.Button(app, text="Exit", command=app.quit, width=30).pack(pady=20)

app.mainloop()
