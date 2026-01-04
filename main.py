import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import font as tkfont
from threading import Thread
import time
import os
import sys
import customtkinter as ctk
import ctypes

CONFIG_FILE = "config.txt"


def resource_path(relative_path):
    try:
        ## PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.Tk()



myappid = 'marindeveloper.undertale.tool' # if you make your own version please change this to your own id but if you arent then please leave it thanks
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


icon_file = resource_path("assets/appicon.ico")
if os.path.exists(icon_file):
    root.iconbitmap(icon_file)


 
font_path = resource_path("assets/PixelOperator.ttf")

if os.path.exists(font_path):
    ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)


root.overrideredirect(True)
root.after(10, lambda: root.set_window_attribute("-topmost", False))  ## if you set this to true it makes it stay on top of all windows, if you want it and it makes it easier to use for streaming then yeah go for it

def show_in_taskbar(window):
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    
    hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    window.wm_withdraw()
    window.after(10, window.wm_deiconify)
    

show_in_taskbar(root)





undertale_font_big = tkfont.Font(family="Pixel Operator", size=36, weight="bold")
undertale_font_small = tkfont.Font(family="Pixel Operator", size=20)
undertale_font_xsmall = tkfont.Font(family="Pixel Operator", size=16)

root.configure(bg="black")

title_bar = ctk.CTkFrame(root, height=35, corner_radius=0, fg_color="black")
title_bar.pack(fill="x", side="top")

title_icon_path = resource_path("assets/appicon.png") 
if os.path.exists(title_icon_path):
    img = tk.PhotoImage(file=title_icon_path)
    icon_label = tk.Label(title_bar, image=img, bg="black")
    icon_label.image = img
    icon_label.pack(side="left", padx=5)
    

# Custom Title Label cuz i need the free promo whenever i get the chance too even tho fucking nobody uses this, if you make your own ver of this app you can change it but if not please leave it thanks
title_label = tk.Label(title_bar, text="Undertale Reset Tool by marindeveloper", 
                       fg="white", bg="black", font=undertale_font_xsmall)
title_label.pack(side="left", padx=5)
# Custom Close Button cuz how you gonna have a window without one
close_button = ctk.CTkButton(title_bar, text="✕", width=40, command=root.destroy, fg_color="transparent", hover_color="red")
close_button.pack(side="right")
def get_pos(event):
    root.xwin = event.x
    root.ywin = event.y

def move_window(event):
    root.geometry(f'+{event.x_root - root.xwin}+{event.y_root - root.ywin}')

title_bar.bind("<Button-1>", get_pos)
title_bar.bind("<B1-Motion>", move_window)




icon_file = resource_path("assets/appicon.ico")
if os.path.exists(icon_file):
    root.iconbitmap(icon_file)

font_path = resource_path("assets/PixelOperator.ttf")

if os.path.exists(font_path):
    ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)



SAVE_FILES = ["file0", "file9", "undertale.ini"]




## FONT NEEDS TO BE INSTALLED ON SYSTEM FOR THE PROGRAM TO LOOK LIKE IT SHOULD ##


path_var = tk.StringVar()

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        saved_path = f.read().strip()
        if os.path.isdir(saved_path):
            path_var.set(saved_path)


reset_count = 0
watching = False

def center_window(win, width=650, height=450):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

center_window(root, 650, 450)


folder_frame = tk.Frame(root, bg="black")
folder_frame.pack(pady=20)

tk.Label(folder_frame, text="Select your UNDERTALE save folder:", fg="white", bg="black", font=undertale_font_small).grid(row=0, column=0, padx=15,sticky="w")

entry_border = tk.Frame(folder_frame, bg="white", bd=0)
entry_border.grid(row=1, column=0, pady=4, padx=15, sticky="we")

entry = tk.Entry(entry_border, textvariable=path_var, width=40, fg="white", bg="black", insertbackground="white", font=undertale_font_small, bd=0, relief="flat")
entry.pack(padx=2, pady=2, fill="x")

def browse_folder():
    folder = filedialog.askdirectory(title="Set up Undertale Reset Tool", initialdir="~")
    if folder:
        path_var.set(folder)

# Browse Button inside folder_frame next to entry
browse_btn_border = tk.Frame(folder_frame, bg="white", bd=0)
browse_btn_border.grid(row=1, column=1, padx=4)

browse_btn = tk.Button(
    browse_btn_border, 
    text="Browse", 
    command=browse_folder, 
    font=undertale_font_small,
    bg="black",      
    fg="white", 
    bd=0,            
    relief="flat",   
    activebackground="white", 
    activeforeground="black",
    padx=10, 
    pady=2,
    cursor="hand2"
)
browse_btn.pack(padx=2, pady=2)


tk.Label(root, text="RESETS:", fg="white", bg="black", font=undertale_font_big).pack(pady=(10,0))
label_count_var = tk.StringVar(value="0")
tk.Label(root, textvariable=label_count_var, fg="white", bg="black", font=undertale_font_big).pack()

def watch_folder(folder):
    global reset_count
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(folder)
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
    start_btn_border.pack_forget()
    change_btn.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
    Thread(target=watch_folder, args=(folder,), daemon=True).start()

start_btn_border = tk.Frame(root, bg="white", bd=0)
start_btn_border.pack(pady=10)

start_btn = tk.Button(
    start_btn_border, 
    text="START WATCHING", 
    command=start_watching, 
    font=undertale_font_small, 
    bg="black",      
    fg="white", 
    bd=0,            
    relief="flat",   
    activebackground="white", 
    activeforeground="black",
    padx=15, 
    pady=5,
    cursor="hand2"
)
start_btn.pack(padx=2, pady=2)

def toggle_folder_frame():
    if folder_frame.winfo_ismapped():
        folder_frame.pack_forget()
    else:
        folder_frame.pack(pady=20, side="top")


def Reset():
    global reset_count

    folder = path_var.get()
    if not folder or not os.path.isdir(folder):
        return

    files_deleted = False

    files_to_delete = [
        "playerachievementcache.dat",
        "system_information_962",
        "system_information_963",
        "file0",
        "file9",
        "file8",
        "undertale.ini"
    ]

    for f in files_to_delete:
        path = os.path.join(folder, f)
        if os.path.exists(path):
            try:
                os.remove(path)
                files_deleted = True
            except Exception:
                pass

    if files_deleted:
        reset_count += 1
        label_count_var.set(str(reset_count))

    
    

reset_btn_border = tk.Frame(root, bg="white", bd=0)
reset_btn_border.pack(pady=10) 

reset_btn = tk.Button(
    reset_btn_border, 
    text="RESET", 
    command=Reset, 
    font=undertale_font_small,
    bg="black",      
    fg="white", 
    bd=0,            
    relief="flat",   
    activebackground="white", 
    activeforeground="black",
    padx=15, 
    pady=5,
    cursor="hand2"
)
reset_btn.pack(padx=2, pady=2)

def on_enter(e): e.widget.config(bg="white", fg="black")
def on_leave(e): e.widget.config(bg="black", fg="white")

for b in [browse_btn, start_btn, reset_btn]:
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)

change_btn = tk.Button(root, text="⚙️", command=toggle_folder_frame, fg="white", bg="black", font=undertale_font_small, bd=0)

root.mainloop()