# Fansim Engine

formerly Pesterquest Modsuite (PQMS)

Tools for writing your own homestuck-style friendsim games in ren'py.

What's included:

- **Package manager**: Write volumes with metadata (credits, warnings, etc) that get intelligently managed. Your volumes won't conflict with other mods *or* other packages written by your team! *This means you can have different people writing different routes at the same time without risk of conflicts.*
- **Homestuck API**: When writing, have loads of convenience functions available! Quirks, dialog boxes, grype, and more.

Design goals:

- Cross-platform (Win/Mac/Linux)
- Easy to write and distribute fan volumes
- Simple for users to play fan volumes
- Maximally accessible
- Mix-and-match: Multiple people can write simultaneously without worrying about naming conflicts



This is written by me, Gio, and it's a labor of love.

If you have any comments, suggestions, complaints, or contributions, you're welcome to reach me on twitter [@giovan_h](https://twitter.com/giovan_h), make an issue here on the [issues](https://github.com/GiovanH/pesterquest-modsuite/issues) page, or even make a pull request if you want to add something new.

**For demo mods and asset packs, see [fse-extras.](https://github.com/GiovanH/fse-extras)**

**For documentation, browse the guides in [the `docs/` folder.](./doc/)**

<!-- MarkdownTOC -->

- [Why FSE?](#why-fse)
    - [Why not FSE?](#why-not-fse)
- [Features](#features)
- [Documentation](#documentation)
- [FAQ](#faq)
- [Examples](#examples)
- [Appendix](#appendix)
    - [Opening a terminal](#opening-a-terminal)
- [Credits](#credits)

<!-- /MarkdownTOC -->

## Why FSE?

The main difference between FSE and straight renpy is FSE exposes a layer between you and the game engine. This is how it provides its many features.

FSE has a slightly different workflow, but as soon as you understand it your project workflow can *drastically* improve. Packages let you organize your workspace and files and easily. Patching systems like this are real-world best practices for programming.

FSE makes you organize your mods as "packages" that *patch* a renpy game rather than replacing it. When you edit screens.rpy, script.rpy, etc from the base game, you risk breaking things. FSE helps you add anything you need without breaking the base game or other mods. Also, it provides a lot of powerful modding features that help greatly with the writing process, so there's a lot you don't need to worry about if you don't want to.

Further, packages are better for users: You don't want to force people to download a large, standalone renpy game for every small fanroute (although you are able to distribute a standalone version, see [here.](./doc/pqlite.md))

You want to edit your MOD, not the game, whenever possible. The more you edit distribution files, the less good FSE is able to do for you. **Don't worry**: You can still do everything you want, including changing the GUI (using litemods).

### Why not FSE?

There are only a few points where FSE is less convenient than simply editing a renpy game:

- Namespacing: FSE encourages you to namespace your names whenever possible by including `__p__` or `!` in the name. For instance, `define jo = Character(...` becomes `define !jo = Character(...` . When FSE runs the patcher, these names are replaced, so two packages can both use the same shortname without conflict.
- The patcher: You need to run `patcher.py` (or `run_wizard.py`, which just launches patcher.py while saving a debug log) to apply changes in your mod files to the game. You *don't* need to run patcher every time you launch the game, or even when pesterquest updates, only when you change modfiles. 

If you already have work done, you can easily convert it into package format either by hand (just changing a few names) or using the automated features in `checker.py`.

**In my opinion, at the end of the day, you should definitely use FSE.**

## Features

a partial list

**Hemospectrum tools** - Don't worry about color codes again!

**Automatic quirk formatting** - You don't have to type gamzee's quirk by hand if you don't want to.

**Dialog tools** - Easily write characters with beautiful nameboxes

**Error recovery** - Fix broken folders and errors, and automatically run safe file cleanup

**Code checking**

**Transcript generation**

**Preprocessor substitution**

## Documentation

See the guides in [the `docs/` folder](./doc/) for detailed documentation.



## FAQ

or, "this is easier than documentation." AMA!



**Q:** I want it! Gimmie it!

**A:** Great! See the [Developer Quickstart](doc/developer_quickstart.md)

**Q:** I updated and everything broke!

**A:** If you have a `liteskins` folder:

1. Rename `liteskins` to `skins`
2. Download and install the ren'py sdk
3. Set the ren'py projects directory to `fansim-engine/projects`

Worst case scenario, make a backup of your custom_volumes folder, delete fse and reinstall.

**Q:** Why should I use this instead of just editing up the rpy files that came with the game--

**A:** *please do not do that.* See [Why FSE?](#why-fse)

Recommended use is to execute the scripts from console while in the `src` folder, but just launching the scripts *should* work in most cases for the patcher and launcher.

**Q:** Can this make hiveswap friendsim style routes too, or just pesterquest routes?

**A:** While the tool is based around pesterquest, *yes*, you can use hiveswap styles, including the hiveswap characters (using the hiveswap package in fse-extras) and the grype gui.

**Q:** My folder is called pesterquest-modsuite, but it's supposed to be called friendsim-engine now?

**A:** This tool used to be called Pesterquest Modsuite, but was renamed. Unless you're getting errors when you update, it should be fine to have old legacy directories that use the old name.

**Q:** Where do I put my music assets?

**A:** FSE does not add any special requirements for the asset types, so put any assets you need to access (music, pictures, etc) in your mod's `assets` folder. For instance, you can have `custom_volumes/xxx/assets/song.mp3` and play it with `play music "{{assets}}/song.mp3"`. It's just as valid to do `custom_volumes/xxx/assets/music/song.mp3` and play it with `play music "{{assets}}/music/song.mp3"`; FSE does not place requirements on your assets' organizational structure.

**Q:** How do I run a python script in a terminal on windows?

**A:** On Windows 10:

- [Open a terminal window](#opening-a-terminal) in your FSE folder
- Type your python command (like `python run_wizard.py --quiet`) and press enter.
  - A python 3.x installation may install as `python3`. If you have errors, try `python3 run_wizard.py --quiet`.
  - There are a few different ways python can install. Try substituting `python` with: `python3`, `py`, `py -3`, or `"C:\Program Files\PythonXX\python.exe"` (where XX is your version, e.g. `37`, `38`)
  - If python is not in your PATH, you still won't be able to launch python. You should [add python to your path](https://duckduckgo.com/?q=add+python+3+to+path&t=vivaldi&ia=web). 

**Q:** Can I package a mod as a standalone distributable that people who don't own pesterquest can play?

**A:** Yes, but this is not recommended. Use `dist_standalone.py`. [Read this document for more details.](./doc/pqlite.md)

**Q:** I packaged my mod as a standalone distributable but I get an error when I run it!

**A:** You're probably referencing assets that are present in the base game. In a standalone distribution, you won't have access to the pesterquest characters, images, or audio: you'll need to manually add those if you want them, or simply distribute the mod normally. Any assets you use will need to have been explicitly provided by a mod. Because of this, **it's really best not to distribute fanroutes standalone unless your project is very large.**

**Q:** Is there any more documentation, besides the online ren'py documentation?

**A:** Browse [the `docs/` folder](./doc/) to see supplemental documentation and tutorials as they're added.

If your question isn't answered here, skim this document and the resources in the `docs/` folder, and if you still have questions, just let me know.


## Examples

Please see the example volumes from [fse-extras](https://github.com/GiovanH/fse-extras) for examples. 

## Appendix

### Opening a terminal

- Navigate to the `src` directory
- `Shift+Right Click` somewhere in the folder, like you would if you were making a new folder.
- In that menu, you'll either see "Open PowerShell Window Here" or "Open Command Prompt Here". Click that.
  - If you opened a powershell window, type `start cmd` and press enter. You are now in a command prompt window.

## Credits

The Befriendus Dev Team (and alienoid) for the "openround" rounded dialog box style as well as the befriendus litestyle.

Alienoid for some documentation contributions, including the `extend` trick in `Mistakes to Avoid`

Gio for everything else here

