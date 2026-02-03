# pkgbuild_parser

[English documentation (GitHub)](https://github.com/KevinCrrl/pkgbuild_parser/blob/main/ingles.md)
[English documentation (Codeberg)](https://codeberg.org/KevinCrrl/pkgbuild_parser/src/branch/main/ingles.md)

## Introduction

**pkgbuild_parser** is a module written in **Python** (compatible with Python 3.x) designed to extract information from a **PKGBUILD**. The main purpose of this module is to provide simple and direct access to the most important fields of a PKGBUILD without relying on external tools or additional libraries.

- **Version:** 1.0.1
- **License:** MIT 2025 KevinCrrl
- **Dependencies:** None
- **Style:** Simplicity, no external dependencies, easy to use

This module allows you to quickly and directly obtain data such as package name, version, description, license, URL, and source file.

---

## Main functions for the user

Although the module internally has support functions (`get_base`), the **user only needs to use the high-level functions**, which are clear and direct:

| Function                               | Description                                                                                               |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `get_pkgname()`                      | Returns the package name (`pkgname`) as a string.                                                       |
| `get_pkgver()`                       | Returns the package version (`pkgver`) as a string.                                                     |
| `get_pkgrel()`                       | Returns the release number (`pkgrel`) as a string.                                                      |
| `get_pkgdesc()`                      | Returns the package description (`pkgdesc`) as a string, removing unnecessary comments and parentheses. |
| `get_arch()`                         | Returns the package architecture (`arch`) as a list of strings.                                         |
| `get_url()`                          | Returns the main project URL (`url`) as a string.                                                       |
| `get_license()`                      | Returns the package license (`license`) as a list of strings.                                           |
| `get_source()`                       | Returns the package source(s) (`source`) as a list of strings.                                          |
| `get_dict_base_info()`               | Returns a dictionary with all the previous fields in the format `{'pkgname': ..., 'pkgver': ..., ...}`. |
| `base_info_to_json()`                | Returns the base information in **JSON** format with indentation and UTF-8 encoding.               |
| `write_base_info_to_json(json_name)` | Writes the base information to a JSON file named `json_name`.                                           |
| `get_epoch()`                        | Returns the package `epoch`.                                                                            |
| `get_full_package_name()`            | Returns the full package name, including `epoch`, version, and `pkgrel`.                              |
| `get_depends()`                      | Returns a list of the package's dependencies.                                                             |
| `get_makedepends()`                  | Returns a list of the package's build dependencies.                                                       |
| `get_optdepends()`                   | Returns a list of the package's optional dependencies.                                                    |
| `get_dict_optdepends()`              | Returns a dictionary of the package's optional dependencies.                                              |
| `optdepends_to_json()`               | Returns a JSON of the package's optional dependencies.                                                    |
| `write_optdepends_to_json()`         | Writes the package's optional dependencies to a JSON file.                                                |
| `get_options()`                      | Returns a list of the package's options.                                                                  |
| `get_checkdepends()`                 | Returns a list of the package's check dependencies.                                                       |
| `get_sha256sums()`                   | Returns a list of the sha256 checksums.                                                                   |
| `get_sha512sums()`                   | Returns a list of the sha512 checksums.                                                                   |
| `get_validpgpkeys()`                 | Returns a list of the valid PGP keys.                                                                     |

**Note:** The internal functions (`get_base` and `multiline`) are intended for module use and **do not need to be used by the user**.

---

## Installation and use

### Option 1: AUR

The module is available on the AUR as **`python-pkgbuild-parser`**.

### Option 2: Manual build

If you want to build it manually:

```bash
python -m build
pip install .
```


## Basic usage

```python
import pkgbuild_parser
import sys

try:
    my_pkgbuild = pkgbuild_parser.Parser("PKGBUILD")
except pkgbuild_parser.ParserFileError as exc:
    print(exc)
    sys.exit(1)

# Get basic data
try:
    print(my_pkgbuild.get_pkgname())
    print(my_pkgbuild.get_pkgver())
    print(my_pkgbuild.get_pkgrel())
    print(my_pkgbuild.get_pkgdesc())
    print(my_pkgbuild.get_arch())
    print(my_pkgbuild.get_url())
    print(my_pkgbuild.get_license())
    print(my_pkgbuild.get_source())
    print(my_pkgbuild.get_epoch())
    print(my_pkgbuild.get_full_package_name())
    print(my_pkgbuild.get_depends())
    print(my_pkgbuild.get_makedepends())
    print(my_pkgbuild.get_optdepends())
    print(my_pkgbuild.get_dict_optdepends())
    print(my_pkgbuild.optdepends_to_json())
    my_pkgbuild.write_optdepends_to_json()
    print(my_pkgbuild.get_options())
    print(my_pkgbuild.get_checkdepends())
    print(my_pkgbuild.get_sha256sums())
    print(my_pkgbuild.get_sha512sums())
    print(my_pkgbuild.get_validpgpkeys())


    # Get a dictionary of all the info
    info = my_pkgbuild.get_dict_base_info()
    print(info)

    # Show in JSON format
    print(my_pkgbuild.base_info_to_json())

    # Get JSON and write it to a file
    my_pkgbuild.write_base_info_to_json("info.json")
except (pkgbuild_parser.ParserKeyError, pkgbuild_parser.ParserNoneTypeError) as e:
    print(e)
```

## Error handling

If the PKGBUILD file does not exist, a `ParserFileError` is raised, which must be caught to prevent the program from failing.

A `ParserKeyError` can also be raised if getting a value from the PKGBUILD fails, for example, if the license is not declared correctly, and `get_license()` is called, this exception will be raised.

Since version 0.2.0, a `ParserNoneTypeError` can also be raised if a function returns `None` when it was not expected.

## Limitations

- The module's goal is to extract only **basic information** from standard PKGBUILDs, it cannot replace bash variables inside another variable, for example, if the source is declared with the value "$url/package.zip".
- It works best with PKGBUILDs that follow the **Arch Wiki** standards.
- Since version 0.4.0, the module can extract information from arrays or lists, such as `depends`, `makedepends`, `source`, `optdepends`, `license`, `options`, and `checkdepends`.
- Since version 1.0.0, functions that return a string no longer include quotes by default.
