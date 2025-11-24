# Undertale-Reset-Counter

A Python tool that automatically monitors your UNDERTALE save folder to detect resets. A reset is counted when the save files are removed and then recreated. It also resets your save with a click of a button!

This tool is designed mainly for speedrunners to keep track of actual resets during their runs. Note that in-game resets do not count unless the save files are deleted from the folder, so normal in-game resets won’t be detected.

# Features

Tracks the number of resets automatically.

Displays resets in a Undertale-ish inspired interface.

A button that resets your UNDERTALE save, basically just deletes the file0, file9, file8, and undertale.ini files.

# Requirements

1. Python 3.x

2. Tkinter

3. Pixel Operator font needs to be installed in order for the program to look correctly. (font is included in files but you could also download from elsewhere)

# Usage

Download the main.py file (and PixelOperator.tff if you haven't already installed this font, download it and install it on your system)

1. Run main.py

2. Select your UNDERTALE save folder.

3. Press Start Watching.

  The reset counter will automatically increment whenever a reset is detected.

  Use the ⚙️ icon to change folders or adjust window settings.
