import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import font as tkfont
from threading import Thread
import time
import os

SAVE_FILES = ["file0", "file9", "undertale.ini"]

root = tk.Tk()
root.title("Undertale Reset Counter by marindeveloper")
root.configure(bg="black")

## FONT NEEDS TO BE INSTALLED ON SYSTEM FOR THE PROGRAM TO LOOK LIKE IT SHOULD ##
undertale_font_big = tkfont.Font(family="Pixel Operator", size=36, weight="bold")
undertale_font_small = tkfont.Font(family="Pixel Operator", size=20)

path_var = tk.StringVar()
reset_count = 0
watching = False

def center_window(win, width=600, height=400):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

center_window(root, 600, 400)

folder_frame = tk.Frame(root, bg="black")
folder_frame.pack(pady=5)

tk.Label(folder_frame, text="Select your UNDERTALE save folder:", fg="white", bg="black", font=undertale_font_small).grid(row=0, column=0, sticky="w")
entry = tk.Entry(folder_frame, textvariable=path_var, width=40, fg="white", bg="black", insertbackground="white", font=undertale_font_small)
entry.grid(row=1, column=0, pady=4, sticky="we")

def browse_folder():
    folder = filedialog.askdirectory(title="Set up Undertale Reset Counter", initialdir="~")
    if folder:
        path_var.set(folder)

browse_btn = tk.Button(folder_frame, text="Browse...", command=browse_folder, fg="black", bg="white", font=undertale_font_small)
browse_btn.grid(row=1, column=1, padx=4)

tk.Label(root, text="RESETS:", fg="white", bg="black", font=undertale_font_big).pack(pady=(30,0))
label_count_var = tk.StringVar(value="0")
tk.Label(root, textvariable=label_count_var, fg="white", bg="black", font=undertale_font_big).pack()

def watch_folder(folder):
    global reset_count
    had_files = any(os.path.exists(os.path.join(folder, f)) for f in SAVE_FILES)
    while watching:
        have_files = any(os.path.exists(os.path.join(folder, f)) for f in SAVE_FILES)
        if had_files and not have_files:
            while not any(os.path.exists(os.path.join(folder, f)) for f in SAVE_FILES):
                if not watching:
                    return
                time.sleep(0.5)
            reset_count += 1
            label_count_var.set(str(reset_count))
        had_files = have_files
        time.sleep(0.5)

def start_watching():
    global watching
    folder = path_var.get()
    if not folder:
        return
    watching = True
    folder_frame.pack_forget()
    start_btn.pack_forget()
    change_btn.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
    Thread(target=watch_folder, args=(folder,), daemon=True).start()

start_btn = tk.Button(root, text="Start Watching", command=start_watching, fg="black", bg="white", font=undertale_font_small)
start_btn.pack(pady=10)

def toggle_folder_frame():
    if folder_frame.winfo_ismapped():
        folder_frame.pack_forget()
    else:
        folder_frame.pack(pady=5, side="top", anchor="nw")

def Reset():
    global reset_count
    folder = path_var.get()
    label_count_var.set(str(reset_count))
    if os.path.exists(f"{folder}\\playerachievementcache.dat"):
        os.remove(f'{folder}\\playerachievementcache.dat')
    if os.path.exists(f"{folder}\\system_information_962"):
        os.remove(f'{folder}\\system_information_962')
    if os.path.exists(f"{folder}\\system_information_963"):
        os.remove(f'{folder}\\system_information_963')
    if os.path.exists(f"{folder}\\file0"):
        os.remove(f'{folder}\\file0')
    if os.path.exists(f'{folder}\\file9'):
        os.remove(f'{folder}\\file9')
    if os.path.exists(f'{folder}\\file8'):
        os.remove(f'{folder}\\file8')
    if os.path.exists(f'{folder}\\undertale.ini'):
        os.remove(f'{folder}\\undertale.ini')
        reset_count += 1
    else:
        reset_count = reset_count
   
    

reset_btn = tk.Button(root, text="Reset", command=Reset, fg="black", bg="white", font=undertale_font_small)
reset_btn.pack(pady=10)


change_btn = tk.Button(root, text="⚙️", command=toggle_folder_frame, fg="white", bg="black", font=undertale_font_small, bd=0)


root.mainloop()
