## Installation

I have two video tutorials that walk you through step 3 up through installing and running mods:

[Version 1: Using terminal commands](https://youtu.be/tMxyXuX_DIA)

[Version 2: Using GUIS](https://youtu.be/qcYgbOkllpE) (if you're uncomfortable with terminals) (Recommended!)

### Installation with git, using the terminal:

Using git is to keep your version of FSE up-to-date is recommended so you have access to all the latest features and development updates.

1. Install a recent version of python (3.6+) if you don't have it installed already. 
   - During setup, make sure to "Add python to your PATH" and install Tkinter, if prompted.
2. Install git for [windows](http://msysgit.github.io/) or [osx](http://git-scm.com/download/mac)
   - When you install git, use the default settings. 
3. Download FSE
   1. Go to a new work folder, for instance `Documents`.
   2. [Open a terminal window](#opening-a-terminal) in that folder.
   3. Run `git clone https://github.com/GiovanH/friendsim-engine`
   4. Congratulations! FSE is installed at `Documents/friendsim-engine`
4. Download FSE Extras (optional)
   1. Starting after step 2.2, run `git clone https://github.com/GiovanH/fse-extras`
   2. Congratulations! Extras are installed at `Documents/fse-extras`


On windows, if you get an error about `'git' is not recognized as an internal or external command, operable program or batch file.` it means git isn't in your PATH. You can reboot, or just run commands in the form of `"C:\Program Files\Git\bin\git" clone https://github.com/GiovanH/friendsim-engine` instead.

Included in FSE and FSE-extras are updater files. On windows, launch `update.bat`, or on osx, launch `update.sh`, and FSE will automatically update itself without deleting any mods or your other files.

Developers can also use standard git commands to update the repository.

Why use git instead of downloading the repository as a zip? Because it makes updating extremely easy, especially compared to manual management.

For more on git, try http://rogerdudler.github.io/git-guide/
