# pkgbuild_parser

[Documentation in Spanish](https://kevincrrl.github.io/KevinCrrl/documentacion/pkgbuild_parser.html)

## Introduction

**pkgbuild_parser** is a module written in **Python** (compatible with Python 3.x) designed to extract information from a **PKGBUILD**. The main purpose of this module is to provide simple and direct access to the most important fields of a PKGBUILD without relying on external tools or additional libraries.

- **Version:** 1.2.0
- **License:** MPL-2.0 2026 KevinCrrl
- **Dependencies:** None
- **Style:** Simplicity, no external dependencies, easy to use

This module allows you to quickly and directly obtain data such as package name, version, description, license, URL, and source file.

---

## Main functions for the user

Although the module internally has support functions (`get_base`), the **user only needs to use the high-level functions**, which are clear and direct:

| Function                                | That returns                                                                                    |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `get_pkgname()`                       | Package name (`pkgname`) as a string.                                                         |
| `get_pkgver()`                        | Package version (`pkgver`) as a string.                                                       |
| `get_pkgrel()`                        | Release number (`pkgrel`) as a string.                                                        |
| `get_pkgdesc()`                       | Package description (`pkgdesc`) as a string.                                                  |
| `get_arch()`                          | Package architecture (`arch`) as a list of strings.                                           |
| `get_url()`                           | Main project URL (`url`) as a string.                                                         |
| `get_license()`                       | Package license (`license`) as a list of strings.                                             |
| `get_source()`                        | Package source(s) (`source`) as a list of strings.                                            |
| `get_dict_base_info()`                | Dictionary with all the previous fields in the format `{'pkgname': ..., 'pkgver': ..., ...}`. |
| `base_info_to_json()`                 | Base information in**JSON** format with indentation and UTF-8 encoding.                   |
| `write_base_info_to_json(json_name)`  | Writes the base information to a JSON file named `json_name`.                                 |
| `get_epoch()`                         | Package `epoch`.                                                                              |
| `get_full_package_name()`             | Full package name, including `epoch`, version, and `pkgrel`.                                |
| `get_depends()`                       | List of the package's dependencies.                                                             |
| `get_makedepends()`                   | List of the package's build dependencies.                                                       |
| `get_optdepends()`                    | List of the package's optional dependencies.                                                    |
| `get_dict_optdepends()`               | Dictionary of the package's optional dependencies.                                              |
| `optdepends_to_json()`                | JSON of the package's optional dependencies.                                                    |
| `write_optdepends_to_json(json_name)` | Writes the package's optional dependencies to a JSON file.                                      |
| `get_options()`                       | List of the package's options.                                                                  |
| `get_checkdepends()`                  | List of the package's check dependencies.                                                       |
| `get_sha256sums()`                    | List of the sha256 checksums.                                                                   |
| `get_sha512sums()`                    | List of the sha512 checksums.                                                                   |
| `get_validpgpkeys()`                  | List of the valid PGP keys.                                                                     |
| `get_conflicts()`                     | List of conflicting packages.                                                                   |
| `get_provides()`                      | List of packages provided.                                                                      |
| `get_replaces()`                      | List of packages it replaces.                                                                   |
| `get_pkgbase()`                       | Base package (`pkgbase`) as a string.                                                         |

**Note:** The internal functions (`get_base` and `multiline`) are intended for module use and **do not need to be used by the user**, except when you want to create functions that are not in the parser.

---

## Installation and use

### Option 1: AUR

The module is available on the AUR as **`python-pkgbuild-parser`**.

### Option 2: PyPi

```
pip install pkgbuild-parser
```

## Basic usage

```python
import pkgbuild_parser
import sys

try:
    my_pkgbuild = pkgbuild_parser.Parser()
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
    print(my_pkgbuild.get_conflicts())
    print(my_pkgbuild.get_provides())
    print(my_pkgbuild.get_replaces())
    print(my_pkgbuild.get_pkgbase())


    # Get a dictionary of all the info
    info = my_pkgbuild.get_dict_base_info()
    print(info)

    # Show in JSON format
    print(my_pkgbuild.base_info_to_json())

    # Get JSON and write it to a file
    my_pkgbuild.write_base_info_to_json("info.json")
except pkgbuild_parser.ParserKeyError as e:
    print(e)
```

## Error handling

If the PKGBUILD file does not exist, a `ParserFileError` is raised, which must be caught to prevent the program from failing.

A `ParserKeyError` can also be raised if getting a value from the PKGBUILD fails, for example, if the license is not declared correctly, and `get_license()` is called, this exception will be raised.

## Limitations and additional notes

- Starting with version 1.2.0, the parser can replace known variables in a Bash string. For example, if you try to fetch a source file and it is declared in the PKGBUILD as "${url}/package-$pkgver.tar.gz", pkgbuild-parser will be able to recognize these variables, retrieve them, and replace them with their values. 
- The module's goal is to extract only **basic information** from standard PKGBUILDs, It cannot replace variables it does not recognize, such as "$my_personal_var", or variations of known variables, such as "$pkgname%suffix".
- It works best with PKGBUILDs that follow the **Arch Wiki** standards.
- Since version 0.4.0, the module can extract information from arrays or lists, such as `depends`, `makedepends`, `source`, `optdepends`, `license`, `options`, and `checkdepends`.
- Since version 1.0.0, functions that return a string no longer include quotes by default.
