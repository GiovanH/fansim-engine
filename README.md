# Pesterquest Modsuite (PQMS)

Tools for modifying and extending pesterquest, and adding your own routes. WIP tools for adding your own routes to pesterquest without breaking the base game or needing a standalone engine!

Design goals:

- Cross-platform (Win/Mac/Linux)
- Easy to write and distribute fan volumes
- Hyper-simple for users to play fan volumes
- Mix-and-match: Put all the fan volumes you want and play routes without conflicts



This is written by me, Gio, and it's a labor of love.

If you have any comments, suggestions, complaints, or contributions, you're welcome to reach me on twitter [@giovan_h](https://twitter.com/giovan_h), make an issue here on the [issues](https://github.com/GiovanH/pesterquest-modsuite/issues) page, or even make a pull request if you want to add something new.

## Guide for users:

1. Download this repository. You can use git or simply download the current version as a zip file.
2. Put the fan volumes you want to use in the `custom_volumes` folder.
3. Run `src/launcher.py` with a recent version of Python.

## FAQ:

or, "this is easier than documentation." AMA!



Q: Why should I use this instead of just editing up the rpy files--

A: **please do not do that.** When you edit screens.rpy, script.rpy, etc from the base game, you risk breaking things. PQMS helps you add anything you need without breaking the base game or other mods. Also, it provides a lot of powerful modding features that help greatly with the writing process, so there's a lot you don't need to worry about if you don't want to.

Q: What's a "recent version of python"?

A: 3.6 or above. Recommended use is to execute the scripts from console while in the `src` folder, but just launching the scripts *should* work in most cases for the patcher and launcher.

Q: Can I package a mod as a standalone distributable that people who don't own pesterquest can play?

A: Yes, actually! Use `dist_standalone.py`. [Read this document for more details.](./doc/pqlite.md)

Q: I packaged my mod as a standalone distributable but I get an error when I run it!

A: You're probably referencing assets that are present in the base game. In a standalone distribution, you won't have access to the pesterquest characters, images, or audio: you'll need to manually add those if you want them, or simply distribute the mod normally. Any assets you use will need to have been explicitly provided by a mod. Because of this, **it's really best not to distribute fanroutes standalone unless your project is very large.**

## Guide for developers:

Incomplete, please see the demo packages in `custom_volumes/` and `custom_volumes_other/`.

Please read the docstrings of the rpy files in `src/sys` for the latest details about features.

The core difficulty is that ren'py dumps all the names into a global namespace, so we need to coordinate to avoid name conflicts.

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
- You might be tempted to ignore all of this. If you do, things may work at first. ***Please do not do this.***

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
4. In any RPY file in your new volume folder, define a `
label {{package_entrypoint}}_sandbox:`, replacing `sandbox` with your volume ID. This is where your volume will start when people select your volume. 
5. Write! 
   - You can write whatever you want in your rpy files, including transformations, labels, menus, etc. 
   - It doesn't matter how your files are organized; you can split them up into multiple files if you want. (Not *quite* true: read about [init offset](https://www.renpy.org/doc/html/python.html?highlight=init%20offset) for more on this.)
   - Be sure to only edit the files in your mod folder; don't go editing anything in a  `game` directory, or anything in the `sys` package. 
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

The Befriendus Dev Team (and alienoid) for the "openround" rounded dialog box style as well as the befriendus litestyle.

Gio for everything else here

