## Package guide

FSE revolves around self-contained packages. This document is an API reference to the available fields and formats.

Packages can contain any number of volumes, which are routes selectable from the extra volume select screen.



All active packages should go in the `custom_volumes` folder.

The `custom_volumes_other` folder is supplied for processing purposes, but volumes in this folder are not loaded.

A simple package could be structured like this:

```
sandbox
├── assets
│   ├── greenscreen.png
│   ├── scourgequest.jpg
│   ├── ...
│   ├── volumeselect_sandbox.png
│   ├── volumeselect_sandbox_small.png
├── assets_common
│   ├── public_image.png
├── credits.yml
├── cronus.rpy
├── main.rpy
└── meta.json
```

There are no additional restrictions on the positions of `.rpy` files, except that the label `__package_entrypoint___{volumeid}` must exist somewhere

### `meta.json`

The `meta.json` file contains basic metadata about your package and defines the volumes. This file is required.

The `package_id` field is the id of the package. It should be unique, and does not need to be concise, as you only needs to use it here.

`volumes` is a list of zero or more volumes the package contains. Each volume has a `volume_id`, which should be unique *within* the package, and other metadata used on the volume select screen.

Volumes also have an **optional** field, "warnings". This should be a string detailing content warnings for the volume, if applicable.

Please note that any quote characters used in `meta.json` need to be escaped with a backslash.

Here is a complete, working example of a `meta.json` file.

```json
{
    "package_id": "gio_dev_sandbox",
    "volumes": [
        {
            "volume_id": "sandbox",
            "title": "Sandbox",
            "subtitle": "\"its free real estate\"",
            "author": "Gio"
        },
        {
            "volume_id": "route",
            "title": "Neprezi",
            "subtitle": "\"K1SS3S FOR M1L3S\"",
            "author": "Gio, Andrew Hussie"
        }
    ]
}
```

### `credits.yml`

`credits.yml` is an extremely flexible file that allows you to credit contributions to your project. It uses the YAML file format.

Crediting formats available are:

DICT: Credits people for specific work they did in a role.

```yaml
DICT:
  {Role}:
    {Person}:
      - {Credit}
    ...
```

Example:

```yaml
DICT:
  Character Artists:
    Amber Cragg:
      - Friendsim Vol 1, 2, 6
    Adrienne Garcia:
      - Friendsim Vol 3, 5, 8, 10-13, 15, 17
```

LIST: Credits people as members of a role

```yaml
LIST:
	{Role}:
		- {Person}
		...
```

Example:

```yaml
LIST:
  Openbound Artists:
    - Amanda H 
    - Chaz Canterbury 
    - Lexxy
    ...
```

POSTSCRIPT: Single lines of text, placed at the end.

Example:

```yaml
POSTSCRIPT:
	- "Made with Ren'py"
```



You can mix and match formats within the file, i.e.

```yaml
DICT:
	...
LIST:
	...
POSTSCRIPT:
	...
```



Note that preprocessor substitutions are allowed, so

```yaml
LIST:
  "{{package_id}}":
    - Gio
```

is valid.

### Other structure

The `assets` folder should contain the assets used only in the package. Assets in the form `assets/greenscreen.png` can be accessed inside your package by loading the displayable `"__p__greenscreen.png"` or `"{{assets}}/greenscreen.png"`.

The `assets_common` folder contains assets that can be used in other packages. Assets in the form `assets_common/greenscreen.png` can be accessed by loading the displayable ``"{{assets_common}}/greenscreen.png"`. Be warned that using the assets_common folder risks name collision! The `assets_common` folder should be **only** be used to expose specific resources, and assets in the folder should use precise, distinct names to reduce the risk of collision.

There are no limits to the file structure of the inside of the `assets` or `assets_common` folder.

The `assets/volumeselect_{volumeid}.png` and `assets/volumeselect_{volumeid}_small.png` images are used to display the volume on the volume select screen. **These files are required.**

