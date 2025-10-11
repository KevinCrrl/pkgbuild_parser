# pkgbuild_parser

## Introduction

**pkgbuild_parser** is a module written in **Python** (compatible with Python 3.x) designed to extract basic information from an **Arch Linux PKGBUILD**.The main purpose of this module is to provide easy and direct access to the most important fields of a PKGBUILD without relying on external tools or additional libraries.

- **Version:** 0.3.1
- **License:** MIT 2025 KevinCrrl
- **Dependencies:** None
- **Style:** Simplicity, no external dependencies, easy to use

This module allows you to quickly and directly obtain data such as the package name, version, description, license, URL, and source file.

---

## Main functions for the user

Although internally the module has helper functions (`get_base`), the **user only needs to use the high-level functions**, which are clear and straightforward:

| Function                                              | Description                                                                                               |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `get_pkgname()`                                     | Returns the package name (`pkgname`) as a string.                                                       |
| `get_pkgver()`                                      | Returns the package version (`pkgver`) as a string.                                                     |
| `get_pkgrel()`                                      | Returns the release number (`pkgrel`) as a string.                                                      |
| `get_pkgdesc()`                                     | Returns the package description (`pkgdesc`) as a string, removing comments and unnecessary parentheses. |
| `get_arch()`                                        | Returns the package architecture (`arch`) as a list of strings.                                                  |
| `get_url()`                                         | Returns the main project URL (`url`) as a string.                                                       |
| `get_license()`                                     | Returns the package license (`license`) as a string, without extra comments or parentheses.             |
| `get_source()`                                      | Returns the package source(s) (`source`) as a list of strings.                                          |
| `get_dict_base_info()`                              | Returns a dictionary with all the previous fields in the format `{'pkgname': ..., 'pkgver': ..., ...}`. |
| `base_info_to_json()`                               | Returns the base information in**JSON** format with indentation and UTF-8 encoding.                 |
| `write_base_info_to_json(json_name)`                | Writes the base information to a JSON file named `json_name`.                                           |
| `remove_quotes(string)`                             | Removes quotes from a string.                                                                             |
| `get_dict_base_info_without_quotes()`               | Returns a dictionary with the base information but without quotes in its values.                          |
| `base_info_to_json_without_quotes()`                | Returns the base information in **JSON** format without quotes in its values.                      |
| `write_base_info_to_json_without_quotes(json_name)` | Writes the base information to a JSON file without quotes in its values.                                  |
| `get_epoch()`                                       | Returns the package `epoch`.                                                                            |
| `get_full_package_name()`                           | Returns the full package name, including `epoch`, version and `pkgrel`.                               | 
| `get_depends()`                                     | Returns a list of the package dependencies.                                                             |
| `get_makedepends()`                                 | Returns a list of the package build dependencies.                                                       |
| `get_optdepends()`                                  | Returns a list of the package optional dependencies.                                                    |
| `get_dict_optdepends()`                             | Returns a dictionary of the package optional dependencies.                                              |

**Note:** The internal functions (`get_base` and `multiline`) are intended for module use and **does not need to be used by the user**.

---

## Installation and usage

### Option 1: AUR

The module is available in the AUR as **`python-pkgbuild-parser`**:

### Option 2: Manual build

If you want to build it manually:

```bash
python -m build
python -m installer --destdir=/installation/path dist/*.whl
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

    # Get a dictionary with all info
    info = my_pkgbuild.get_dict_base_info()
    print(info)

    # Show JSON format
    print(my_pkgbuild.base_info_to_json())

    # Save JSON to file
    my_pkgbuild.write_base_info_to_json("info.json")

    # Using remove_quotes
    string_with_quotes = my_pkgbuild.get_pkgdesc()
    string_without_quotes = pkgbuild_parser.remove_quotes(string_with_quotes)
    print(f"Original string: {string_with_quotes}")
    print(f"String without quotes: {string_without_quotes}")
except (pkgbuild_parser.ParserKeyError, pkgbuild_parser.ParserNoneTypeError) as e:
    print(e)
```

## Error handling

If the PKGBUILD file does not exist, a `ParserFileError` is thrown, which must be caught to prevent the program from crashing.

A `ParserKeyError` may also be thrown if obtaining a value from the PKGBUILD fails; for example, if the license is not properly declared, and call get_license(), this exception will occur.

Since version 0.2.0, a `ParserNoneTypeError` can also be raised if a function returns `None` when it was not expected.

## Limitations

- The module's purpose is to extract only **basic information** from a standard PKGBUILD.
- Works best with PKGBUILDs that follow the **Arch Wiki** standards.
- Since version 0.3.0, the module can extract information from arrays or lists, such as `depends`, `makedepends`, `source` and `optdepends`.