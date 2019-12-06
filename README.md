# pesterquest-modsuite v0.7.0
Tools for modifying and extending pesterquest, and adding your own routes
WIP tools for adding your own routes to pesterquest without breaking the base game or needing a standalone engine!

Design goals:

- Cross-platform (Win/Mac/Linux)
- Easy to write and distribute fan volumes
- Hyper-simple for users to play fan volumes
- Mix-and-match: Put all the fan volumes you want and play routes without conflicts

## Guide for users:

Download this repository, put the fan volumes you want in the `custom_volumes` folder, and run `src/launcher.py` with a recent version of Python.

## FAQ:

Q: What's a "recent version of python"?

A: 3.6 or above

Q: 

AMA

## Technical notes:

This does not overwrite any game files and should be compatable with all future updates!
The only content this overrides is the main menu to add a menu option. (Here, just a plain `> ` for now.)
You cannot use any of this to pirate pesterquest. 

## Guide for developers:

Incomplete, please see the demo packages in `custom_volumes/` and `custom_volumes_other/`.

The core difficulty is that ren'py dumps all the names into a global namespace, so we need to coordinate to avoid name conflicts.

## Features
**Preprocessor substitution**

In order to help you avoid namespace conflicts, the patcher runs a text preprocessor on your files. The following substitutions are availible:

- `{{assets}}`: Points to the package-level assets folder. Use this as your `assets` folder, the folder containing assets unique to your package.
- `{{asssets_commmon}}`: Points to the common assets folder identified by `assets_common`. Use this sparingly and remember to namespace any assets you put here.
- `{{p}}` and `__p__`: Interchangable. These are a package-specific prefix: define names starting with these to avoid namespace conflicts. The latter version is provided for ease in syntax highlighting. 
- `{{package_id}}`: This is the unique ID of your package, for use in other areas. Be careful: this is not guaranteed to have any relation to the package-specific prefix!
- `{{package_entrypoint}}`: This is the the first part of your entry label. PQMS will direct players to the label `{{package_entrypoint}}_{route_id}` when they start your route. Note that `{route_id}` is *not* a preprocessor substituion; you will need to fill this in manually.

### What's in the box:

- `launcher.py`: This runs `patcher.py` while logging all output to file.
- `patcher.py`: This is the main script that compiles custom volumes and patches them into the main game. 
- `checker.py`: This script is meant as a helper to read through volumes and detect possible issues. 
- `package.py`: This script allows you to compile custom volumes and assets into minified versions for packaging and distribution.
- `dist_standalone.py`: This script allows you to package your mod as a standalone application for people who don't own pesterquest. ***This will not let you pirate pesterquest.*** Support WP!

### A basic workflow

1. Create a new volume in `custom_volumes`. You can use the example volumes as a template.
2. Edit `meta.json`. `package_id` should be a unique identifier for the package, while each volume (route, selectable from the menu) should have a unique `volume_id`. Try not to pick ids other people might use.
3. Rename your volume select icon in `assets` to `volumeselect_{volume_id}_idle.png` and `volumeselect_{volume_id}_small.png`, and design them as desired.
4. In any RPA file in your new volume folder, define a `
label {{package_entrypoint}}_sandbox:`, replacing `sandbox` with your volume ID. This is where your volume will start when people select your volume. 
5. Write!
6. Run `launcher.py` to test and run your mod. You can use command line arguments to control game launch and other features. 
7. To see your changes live, run `launcher.py --nolaunch` and then press `Shift+R` while in-game to automatically reload.


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

## Example

Please see the example volumes for examples. 

l33t hacker notes:
- The system data is loaded first, so any custom volume content can replace it. You can use this to reskin the menu and other system assets. 
- patcher.py is a preprocessor that, among other features, runs a simple substitution based on subtable.json *on your whole script*. 

## Standard init offsets

0: Reserved for system and library definitions that depend on pesterquest
1: Reserved for definitions that depend on system and library definitions
2: Require assets to be defined first

## Credits

The Befriendus Dev Team (and alienoid) for the "openround" rounded dialog box style

Gio for everything else here

