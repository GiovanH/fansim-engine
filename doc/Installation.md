## Installation

### Installation with git: (Recommended)

Using git is to keep your version of PQMS up-to-date is recommended so you have access to all the latest features and development updates.

1. Install a recent version of python (3.6+) if you don't have it installed already. 
   - During setup, make sure to "Add python to your PATH" and install Tkinter, if prompted.
2. Install git for [windows](http://msysgit.github.io/) or [osx](http://git-scm.com/download/mac)
   - When you install git, use the default settings. 
3. Download PQMS
   1. Go to a new work folder, for instance `Documents`.
   2. [Open a terminal window](#opening-a-terminal) in that folder.
   3. Run `git clone https://github.com/GiovanH/pesterquest-modsuite`
   4. Congratulations! PQMS is installed at `Documents/pesterquest-modsuite`
4. Download PQMS Extras (optional)
   1. Starting after step 2.2, run `git clone https://github.com/GiovanH/pqms-extras`
   2. Congratulations! Extras are installed at `Documents/pesterquest-modsuite`

I have two video tutorials that walk you through step 3 up through installing and running mods:

[Version 1: Using terminal commands](https://youtu.be/tMxyXuX_DIA)

[Version 2: Using GUIS](https://youtu.be/qcYgbOkllpE) (if you're uncomfortable with terminals)

On windows, if you get an error about `'git' is not recognized as an internal or external command, operable program or batch file.` it means git isn't in your PATH. You can reboot, or just run commands in the form of `"C:\Program Files\Git\bin\git" clone https://github.com/GiovanH/pesterquest-modsuite` instead.

Included in PQMS and PQMS-extras are updater files. On windows, launch `update.bat`, or on osx, launch `update.sh`, and PQMS will automatically update itself without deleting any mods or your other files.

Developers can also use standard git commands to update the repository.

Why use git instead of downloading the repository as a zip? Because it makes updating extremely easy, especially compared to manual management.

For more on git, try http://rogerdudler.github.io/git-guide/