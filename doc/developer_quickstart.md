# Developer Quickstart

## Installation

### Installation with git, using the terminal:

Using git is to keep your version of FSE up-to-date is recommended so you have access to all the latest features and development updates.

1. Install a recent version of python (3.6+) if you don't have it installed already. 
   - During setup, make sure to "Add python to your PATH" and install Tkinter, if prompted.
2. Install git for [windows](http://msysgit.github.io/) or [osx](http://git-scm.com/download/mac)
   - When you install git, you can safely use the default settings. 
3. Download FSE
   1. Go to a new work folder, for instance `Documents`.
   2. [Open a terminal window](#opening-a-terminal) in that folder.
   3. Run `git clone https://github.com/GiovanH/fansim-engine`
   4. Congratulations! FSE is installed at `fansim-engine`
4. Download and configure the Ren'py sdk
   1. Download the ren'py SDK from https://www.renpy.org/latest.html and extract it
   2. Open the SDK and under preferences, set your Projects Directory to `fansim-engine/projects` (whereever you cloned the fansim-engine project)


On windows, if you get an error about `'git' is not recognized as an internal or external command, operable program or batch file.` it means git isn't in your PATH. You can reboot, or just run commands in the form of `"C:\Program Files\Git\bin\git" clone https://github.com/GiovanH/fansim-engine` instead.

Included in FSE and FSE-extras are updater files. On windows, launch `update.bat`, or on osx, launch `update.sh`, and FSE will automatically update itself without deleting any mods or your other files. Developers can also use standard git commands (pull) to update the repository.

We use git instead of just downloading there repository as a zip because git makes updating extremely easy, especially compared to manual management. For more on git, try http://rogerdudler.github.io/git-guide/

### A basic workflow

1. Create a new volume in `custom_volumes`. You can use an example volume from fse-extras as a template. The volume is correctly placed when you have a path like `fansim-engine/custom_volumes/myvolume/meta.json`.
2. Edit `meta.json`. `package_id` should be a unique identifier for the package, while each volume (route, selectable from the menu) should have a unique `volume_id`. Try not to pick ids other people might use.
3. Rename your volume select icon in `assets` to `volumeselect_{volume_id}_idle.png` and `volumeselect_{volume_id}_small.png`, and design them as desired.
4. In any RPY file in your new volume folder, define a `
   label {{package_entrypoint}}_sandbox:`, replacing `sandbox` with your volume ID. This is where your volume will start when people select your volume. 
5. Write! 
   - You can write whatever you want in your rpy files, including transformations, labels, menus, etc. 
   - It doesn't matter how your files are organized; you can split them up into multiple files if you want. (Not *quite* true: read about [init offset](https://www.renpy.org/doc/html/python.html?highlight=init%20offset) for more on this.)
   - **Be sure to only edit the files in your mod folder; don't go editing anything in a `projects` or `game` directory, or anything in the `sys` package.** See: [Why FSE](#why-fse)?
6. Run `run_wizard.py` or `run_wizard_gui.py` to compile your mod. You can use command line arguments to control game launch and other features.
7. Launch the game by opening the renpy sdk, selecting the "work" project, and clicking "Launch" 
8. To see your changes live, re-run the wizard and then press `Shift+R` while in-game to reload.
9. When you're ready to distribute your mod, you can package your mod as a standalone game using `dist_standalone.py`, or just share your `litedist` folder directly, if you want. More advanced users can also share the mod folder with other developers.


Developing with this basically the same as extending ren'py using the base game, with a few exceptions for the package manager:

- Each subfolder in the `custom_volumes` folder is a **package**.
- Each package can have any number of **volumes**, or **routes**. These are the icons that appear on the selection page, and they take you to labels in the code.
- You hook your route into the main menu by making sure you've done the following:
  - Your package has a meta.json file that identifies each volume
  - Your source code has a line like `label {{package_entrypoint}}_vid:` where `vid` is the volume ID
- Source files in `{package}/*.rpy` are copied to `{pesterquest}/game/custom_vol_{package_id}_*.rpy`
- Assets in `{package}/assets` are copied to `{pesterquest}/game/custom_assets_{package_id}/`
- Assets in `{package}/assets_common` are copied to `{pesterquest}/game/custom_assets/`
- For each route/volume, you should have a `volumeselect_{tileid}_idle.png` and `volumeselect_{tileid}_small.png` image for the character select screen in its assets folder.

Please see the implementation in `patcher.py` and the demo route for more details.
Updates and contributions to this guide, as well as suggestions for logic rework are all very much appreciated. 
