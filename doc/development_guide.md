# Developer notes

Incomplete, please see the demo packages in `custom_volumes/` and `custom_volumes_other/`.

Please read the [docstrings](doc/docstrings.txt) of the rpy files in `src/sys` for the latest details about features.

The core difficulty is that ren'py dumps all the names into a global namespace, so we need to coordinate to avoid name conflicts.

The system data is loaded first, so any custom volume content can replace it. You can use this to reskin the menu and other system assets. 

patcher.py is a preprocessor that, among other features, runs a simple substitution based on subtable.json *on your whole script*. 

## Features

a partial list

**Hemospectrum tools** - Don't worry about color codes again!

**Automatic quirk formatting** - You don't have to type gamzee's quirk by hand if you don't want to.

**Dialog tools** - Easily write characters with beautiful nameboxes

**Error recovery** - Fix broken folders and errors, and automatically run safe file cleanup

**Code checking**

**Transcript generation**

**Preprocessor substitution**

In order to help you avoid namespace conflicts, the patcher runs a text preprocessor on your files. The following substitutions are available:

- `{{assets}}`: Points to the package-level assets folder. Use this as your `assets` folder, the folder containing assets unique to your package.
- `{{asssets_commmon}}`: Points to the common assets folder identified by `assets_common`. Use this sparingly and remember to namespace any assets you put here.
- `{{p}}` and `__p__`: Interchangeable. These are a package-specific prefix: define names starting with these to avoid namespace conflicts. The latter version is provided for ease in syntax highlighting. 
- `!` is shorthand for `__p__`, and is recommended for names that can be namespace with dots, like characters. However, in order to avoid accidental substitutions of dialogue, it can only be used in name definitions and start-of-line character calls.
- `{{package_id}}`: This is the unique ID of your package, for use in other areas. Be careful: this is not guaranteed to have any relation to the package-specific prefix!
- `{{package_entrypoint}}`: This is the the first part of your entry label. FSE will direct players to the label `{{package_entrypoint}}_{route_id}` when they start your route. Note that `{route_id}` is *not* a preprocessor substitution; you will need to fill this in manually.

TLDR:

- All your custom names (labels, defines, characters, transforms, image ids, etc) should have `__p__` somewhere in the name so fse can prevent conflicts for you
- The package entrypoint must conform exactly to either ``{{package_entrypoint}}_{route_id}`` or ``__package_entrypoint___{route_id}``. (Two, one, three underscores.)
- You might be tempted to ignore all of this. If you do, things may work at first. ***Please do not do this.*** See [Why FSE?](#why-fse)



Substitution examples, with a demo package sandbox:

| Your file           | Renpy sees                   |
| ------------------- | ---------------------------- |
| `image !avatar =`   | `image sandbox_avatar =`     |
| `"!avatar"`         | `"!avatar"` (No replacement) |
| `"__p__avatar"`     | `"sandbox_avatar"`           |
| `define __p__.jo =` | `define sandbox_.jo`         |
| `define !.jo =`     | `define sandbox_.jo`         |
| `define __p__jo =`  | `define sandbox_jo`          |
| `define !jo =`      | `define sandbox_jo`          |



## What's in the box

- `run_wizard.py`: This runs `patcher.py` while logging all output to file.
- `patcher.py`: This is the main script that compiles custom volumes and patches them into the main game. 
- `checker.py`: This script is meant as a helper to read through volumes and detect possible issues. 
- `package.py`: This script allows you to compile custom volumes and assets into minified versions for packaging and distribution.
- `dist_standalone.py`: This script allows you to package your mod as a standalone application for people who don't own pesterquest. ***This will not let you pirate pesterquest.*** Support WP!

## Standard init offsets

Including the line `init offset = [x]` changes the load order of your files. Read this if you're experiencing errors about names not being defined when you launch renpy, or if you're just interested.

If you define characters, styles, or transforms in a separate file from your script, it should start with `init offset = 1`.

In general your scripts should start with `init offset = 2`.

0: Reserved for system and library definitions that depend on the base game.  
1: Require the base game and FSE supplemental assets to be loaded first.  
2: Require all assets to be loaded first.