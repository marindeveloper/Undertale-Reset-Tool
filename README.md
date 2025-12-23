## Undertale Reset Tool
A lightweight Python tool that automatically monitors your UNDERTALE save folder to detect and count resets. 

Designed specifically for speedrunners to keep track of **True Resets** (where save files are physically deleted) so that each run can be legal. In-game resets do NOT count as they don't delete files from the folders, this also means a True Reset wasn't done and the run is not legal.

---
<img width="550" height="405" alt="Screenshot 2025-12-23 195848" src="https://github.com/user-attachments/assets/6112ed6b-8b32-466e-8ebf-9084332cede8" />


## Download & Installation
If you just want to use the tool as is, you don't need to install anything else.

1. Go to the [Releases](https://github.com/marindeveloper/Undertale-Reset-Tool/releases) page.
2. Download the latest `Undertale-Reset-Tool.zip`.
3. Extract the folder and run `Undertale Reset Tool.exe`.

> **⚠️ Antivirus Note:** Some antivirus software may flag the EXE as a false positive. This is a common issue with Python apps built with PyInstaller. You can verify the safety by checking the source code here (it's only 283 lines so), by uploading it to virustotal or well you can do anything you want lol it's open source.



## Features
* **Auto-Detection:** Automatically increments the counter when save files are deleted and recreated.
* **True Reset Button:** Clears all Undertale save data (`file0`, `file9`, `undertale.ini`, etc.) with one click.
* **Undertale Aesthetic:** Custom UI inspired by the game’s style.
* **Customizable:** Change your save folder at any time using the ⚙️ icon.



##  Usage
1. **Set Folder:** Launch the app and select your UNDERTALE save folder (usually in `AppData/Local/UNDERTALE`).
2. **Watch:** Press **START WATCHING**. The counter will now track file changes.
3. **Reset:** Use the **RESET** button in the app to perform a legal speedrun reset. 
   * *Note: In-game menu resets do not trigger the counter as they do not delete the physical files.*



## Requirements (For Developers)
If you want to run the script from source or modify it:

1. **Python 3.x**
2. **External Libraries:** You must install the following via terminal/command prompt:
   ```bash
   pip install customtkinter.
   ```
3. **Font:** The **Pixel Operator** font is required. (unless you're using the code for your own project then you can use whatever font you may want.) 
   * It is included in the `assets/` folder.
   * You can also download it from [Dafont](https://www.dafont.com/pixel-operator.font).
   * 
### How to Run from Source
1. Clone the repo.
2. Ensure the `assets/` folder is in the same directory as `main.py`.
3. Run `python main.py`.



## Credits
*If you use the code for your own project, please keep the credit in the title bar!*
