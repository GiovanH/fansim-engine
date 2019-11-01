# pesterquest-modsuite
Tools for modifying and extending pesterquest, and adding your own routes
WIP tools for adding your own routes to pesterquest without breaking the base game or needing a standalone engine!

![Example menu](./doc/pq_c.gif)

![Example route](./doc/8itch.png)

## Technical notes:

This does not overwrite any game files and should be compatable with all future updates!
The only content this overrides is the main menu to add a menu option. (Here, just a plain `> ` for now.)
You cannot use any of this to pirate pesterquest. 

## Guide for users:

Download this repository, put the fan volumes you want in the `src/custom_volumes` folder, and run `patch_and_run.py` with a recent version of Python.

## Guide for developers:

Incomplete, please see the demo route in `src/custom_volumes/vriska`.

It's basically the same as extending ren'py using the base game, with a few exceptions for the package manager:
- Each subfolder in the `custom_volumes` folder is a **package**.
- Each package can have any number of **routes** (referred to internally as **volumes**; sorry for the confusion)
- You hook your route into the main menu by making sure you've done the following:
    - Your package has a meta.json file that identifies each route
    - Your meta.json file has the **label** of your script's starting point as it's "entrypoint"
    - You have 
- Source files in `{package}/*.rpy` are copied to `{pesterquest}/game/custom_vol_{package_id}_*.rpy`
- Assets in `{package}/assets` are copied to `{pesterquest}/game/custom_assets_{package_id}/`
- Assets in `{package}/assets_common` are copied to `{pesterquest}/game/custom_assets/`
- For each route/volume, you should have a `volumeselect_{tileid}_idle.png` and `volumeselect_{tileid}_small.png` image for the character select screen

Please see the implementation in `patch_and_run.py` and the demo route for more details.
Updates and contributions to this guide, as well as suggestions for logic rework are all very much appreciated. 
