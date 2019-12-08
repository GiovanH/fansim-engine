# Pesterquest Modsuite (PQMS)

Tools for modifying and extending pesterquest, and adding your own routes. WIP tools for adding your own routes to pesterquest without breaking the base game or needing a standalone engine!

Design goals:

- Cross-platform (Win/Mac/Linux)
- Easy to write and distribute fan volumes
- Hyper-simple for users to play fan volumes
- Mix-and-match: Put all the fan volumes you want and play routes without conflicts!



This is written by me, Gio, and it's a labor of love.

If you have any comments, suggestions, complaints, or contributions, you're welcome to reach me on twitter [@giovan_h](https://twitter.com/giovan_h), make an issue here on the [issues](https://github.com/GiovanH/pesterquest-modsuite/issues) page, or even make a pull request if you want to add something new.

**For demo mods and asset packs, see [pqms-extras](https://github.com/GiovanH/pqms-extras)**

## Guide for users:

1. Download this repository. You can use git or simply download the current version as a zip file.
2. Put the fan volumes you want to use in the `custom_volumes` folder.
3. Run `src/run_wizard.py` with a recent version of Python.

## Why PQMS?

The main difference between PQMS and straight renpy is PQMS exposes a layer between you and the game engine. This is how it provides its many features.

PQMS has a slightly different workflow, but as soon as you understand it your project workflow can *drastically* improve. Packages let you organize your workspace and files and easily. Patching systems like this are real-world best practices for programming.

PQMS makes you organize your mods as "packages" that *patch* a renpy game rather than replacing it. When you edit screens.rpy, script.rpy, etc from the base game, you risk breaking things. PQMS helps you add anything you need without breaking the base game or other mods. Also, it provides a lot of powerful modding features that help greatly with the writing process, so there's a lot you don't need to worry about if you don't want to.

Further, packages are better for users: You don't want to force people to download a large, standalone renpy game for every small fanroute (although you are able to distribute a standalone version, see [here.](./doc/pqlite.md))

You want to edit your MOD, not the game, whenever possible. The more you edit distribution files, the less good PQMS is able to do for you. **Don't worry**: You can still do everything you want, including changing the GUI (using litemods).

## Why not PQMS?

There are only a few points where PQMS is less convenient than simply editing a renpy game:

- Namespacing: PQMS encourages you to namespace your names whenever possible by including `__p__` in the name. For instance, `define jo = Character(...` becomes `define __p__jo = Character(...` or `define jo__p__ = Character(...`. When PQMS runs the patcher, these names are replaced, so two packages can both use the same shortname without conflict.
- The patcher: You need to run `patcher.py` (or `run_wizard.py`, which just launches patcher.py while saving a debug log) to apply changes in your mod files to the game. You *don't* need to run patcher every time you launch the game, or even when pesterquest updates, only when you change modfiles. 

If you already have work done, you can easily convert it into package format either by hand (just changing a few names) or using the automated features in `checker.py`.

**You should definitely use PQMS.**



## FAQ:

or, "this is easier than documentation." AMA!



**Q:** I want it! Gimmie it!

**A:** Great! See [Installation](#installation)

**Q:** Why should I use this instead of just editing up the rpy files that came with the game--

**A:** *please do not do that.* See [Why PQMS?](#why-pqms)

**Q:** What's a "recent version of python"?

**A:** 3.6 or above. [You should download the latest stable version for windows](https://www.python.org/downloads/) and add python to your PATH during installation. 

Recommended use is to execute the scripts from console while in the `src` folder, but just launching the scripts *should* work in most cases for the patcher and launcher.

**Q:** How do I run a python script in a terminal on windows?

**A:** On Windows 10:

- [Open a terminal window](#opening-a-terminal) in your PQMS folder
- Type your python command (like `python run_wizard.py --quiet`) and press enter.
  - A python 3.x installation may install as `python3`. If you have errors, try `python3 run_wizard.py --quiet`.
  - If python is not in your PATH, you still won't be able to launch python. You should [add python to your path](https://duckduckgo.com/?q=add+python+3+to+path&t=vivaldi&ia=web). 

**Q:** Can I package a mod as a standalone distributable that people who don't own pesterquest can play?

**A:** Yes, but this is not recommended. Use `dist_standalone.py`. [Read this document for more details.](./doc/pqlite.md)

**Q:** I packaged my mod as a standalone distributable but I get an error when I run it!

**A:** You're probably referencing assets that are present in the base game. In a standalone distribution, you won't have access to the pesterquest characters, images, or audio: you'll need to manually add those if you want them, or simply distribute the mod normally. Any assets you use will need to have been explicitly provided by a mod. Because of this, **it's really best not to distribute fanroutes standalone unless your project is very large.**

**Q:** Is there any more documentation, besides the online ren'py documentation?

**A:** Browse [the `docs/` folder](https://github.com/GiovanH/pesterquest-modsuite/tree/master/doc) to see supplemental documentation and tutorials as they're added.

## Installation

### Installation with git: (Recommended)

Using git is to keep your version of PQMS up-to-date is recommended so you have access to all the latest features and development updates.

1. Install git for [windows](http://msysgit.github.io/) or [osx](http://git-scm.com/download/mac)
2. Download PQMS
   1. Go to a new work folder, for instance `Documents`.
   2. [Open a terminal window](#opening-a-terminal) in that folder.
   3. Run `git clone https://github.com/GiovanH/pesterquest-modsuite`
   4. Congratulations! PQMS is installed at `Documents/pesterquest-modsuite`
3. Download PQMS Extras (optional)
   1. Starting after step 2.2, run `git clone https://github.com/GiovanH/pqms-extras`
   2. Congratulations! Extras are installed at `Documents/pesterquest-modsuite`

Why use git? Because it makes updating extremely easy.

Included in PQMS and PQMS-extras are updater files. On windows, launch `update.bat`, or on osx, launch `update.sh`, and PQMS will automatically update itself without deleting any mods or your other files.

Developers can also use standard git commands to update the repository.

For more on git, try http://rogerdudler.github.io/git-guide/

## Features
a partial list

**Hemospectrum tools**

**Automatic quirk formatting**

**Dialog tools**

**Preprocessor substitution**

In order to help you avoid namespace conflicts, the patcher runs a text preprocessor on your files. The following substitutions are available:

- `{{assets}}`: Points to the package-level assets folder. Use this as your `assets` folder, the folder containing assets unique to your package.
- `{{asssets_commmon}}`: Points to the common assets folder identified by `assets_common`. Use this sparingly and remember to namespace any assets you put here.
- `{{p}}` and `__p__`: Interchangeable. These are a package-specific prefix: define names starting with these to avoid namespace conflicts. The latter version is provided for ease in syntax highlighting. 
- `{{package_id}}`: This is the unique ID of your package, for use in other areas. Be careful: this is not guaranteed to have any relation to the package-specific prefix!
- `{{package_entrypoint}}`: This is the the first part of your entry label. PQMS will direct players to the label `{{package_entrypoint}}_{route_id}` when they start your route. Note that `{route_id}` is *not* a preprocessor substitution; you will need to fill this in manually.

TLDR:

- All your custom names (labels, defines, characters, transforms, image ids, etc) should have `__p__` somewhere in the name so pqms can prevent conflicts for you
- The package entrypoint must conform exactly to either ``{{package_entrypoint}}_{route_id}`` or ``__package_entrypoint___{route_id}``. (Two, one, three underscores.)
- You might be tempted to ignore all of this. If you do, things may work at first. ***Please do not do this.*** See [Why PQMS?](#why-pqms)

### What's in the box:

- `run_wizard.py`: This runs `patcher.py` while logging all output to file.
- `patcher.py`: This is the main script that compiles custom volumes and patches them into the main game. 
- `checker.py`: This script is meant as a helper to read through volumes and detect possible issues. 
- `package.py`: This script allows you to compile custom volumes and assets into minified versions for packaging and distribution.
- `dist_standalone.py`: This script allows you to package your mod as a standalone application for people who don't own pesterquest. ***This will not let you pirate pesterquest.*** Support WP!

### A basic workflow

1. Create a new volume in `custom_volumes`. You can use the example volumes as a template.
2. Edit `meta.json`. `package_id` should be a unique identifier for the package, while each volume (route, selectable from the menu) should have a unique `volume_id`. Try not to pick ids other people might use.
3. Rename your volume select icon in `assets` to `volumeselect_{volume_id}_idle.png` and `volumeselect_{volume_id}_small.png`, and design them as desired.
4. In any RPY file in your new volume folder, define a `
label {{package_entrypoint}}_sandbox:`, replacing `sandbox` with your volume ID. This is where your volume will start when people select your volume. 
5. Write! 
   - You can write whatever you want in your rpy files, including transformations, labels, menus, etc. 
   - It doesn't matter how your files are organized; you can split them up into multiple files if you want. (Not *quite* true: read about [init offset](https://www.renpy.org/doc/html/python.html?highlight=init%20offset) for more on this.)
   - **Be sure to only edit the files in your mod folder; don't go editing anything in a `litedist`, `dist`, or `game` directory, or anything in the `sys` package.** See: [Why PQMS](#why-pqms)?
6. Run `run_wizard.py` to test and run your mod. You can use command line arguments to control game launch and other features. 
7. To see your changes live, run `run_wizard.py --nolaunch` and then press `Shift+R` while in-game to automatically reload.
8. When you're ready to distribute your mod, you can zip and distribute your mod folder (`custom_volumes/xxx`). You can also package your mod as a standalone game using `dist_standalone.py`, but this is not recommended for general use.


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

## Developer notes:

Incomplete, please see the demo packages in `custom_volumes/` and `custom_volumes_other/`.

Please read the [docstrings](doc/docstrings.txt) of the rpy files in `src/sys` for the latest details about features.

The core difficulty is that ren'py dumps all the names into a global namespace, so we need to coordinate to avoid name conflicts.

The system data is loaded first, so any custom volume content can replace it. You can use this to reskin the menu and other system assets. 

patcher.py is a preprocessor that, among other features, runs a simple substitution based on subtable.json *on your whole script*. 

### Standard init offsets

Including the line `init offset = [x]` changes the load order of your files. Read this if you're experiencing errors about names not being defined when you launch renpy, or if you're just interested.

If you define characters, styles, or transforms in a separate file from your script, it should start with `init offset = 1`.

In general your scripts should start with `init offset = 2`.

0: Reserved for system and library definitions that depend on the base game.
1: Require the base game and PQMS supplemental assets to be loaded first.
2: Require all assets to be loaded first.

## Examples

Please see the example volumes from [pqms-extras](https://github.com/GiovanH/pqms-extras) for examples. 

## Appendix

### Opening a terminal

- Navigate to the `src` directory
- `Shift+Right Click` somewhere in the folder, like you would if you were making a new folder.
- In that menu, you'll either see "Open PowerShell Window Here" or "Open Command Prompt Here". Click that.
  - If you opened a powershell window, type `start cmd` and press enter. You are now in a command prompt window.

## Credits

The Befriendus Dev Team (and alienoid) for the "openround" rounded dialog box style as well as the befriendus litestyle.

Gio for everything else here

