#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from platform import machine


class ParserFileError(Exception):
    pass


class ParserKeyError(Exception):
    pass


def remove_quotes(string) -> list[str] | str:
    if isinstance(string, list):
        return string
    new_string = ""
    for char in string:
        if char not in ("'", '"'):
            new_string += char
    return new_string


class ParserCore:
    __slots__ = ('filename', 'lines')

    def __init__(self, filename: str = "PKGBUILD"):
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                self.lines = [line.strip() for line in f]
        except FileNotFoundError as exc:
            raise ParserFileError(f"PKGBUILD file '{filename}' not found") from exc

    def multiline(self, key: str) -> list[str]:
        list_of_lines: list[str] = []
        key_found: bool = False
        for line in self.lines:
            # line example: optdepends=('package: desc' # comment
            # or
            # line example: optdepends=('one_package: one_desc') # comment

            # new line example: optdepends=(one_package: one_desc) or optdepends=(package: desc
            line: str = remove_quotes(line.split("#")[0].strip())
            if not key_found and line.startswith(f"{key}="):  # key discovered
                # fix for depends and makedepends
                if " " in line and ":" not in line:
                    list_of_lines = line.split()
                    list_of_lines[0] = list_of_lines[0].split("=(")[1]
                else:
                    list_of_lines.append(line.split("=")[1].lstrip("(").rstrip(
                        " "))  # new line example: one_package: one_desc) or package: desc
                key_found = True
            if key_found and list_of_lines[0].endswith(")"):
                # Fix for optdepends arrays
                if ":" in list_of_lines[0]:
                    list_of_lines[0] = list_of_lines[0].rstrip(")")
                else:
                    list_of_lines = list_of_lines[0].rstrip(")").split()
                list_of_lines = [package.strip() for package in list_of_lines]  # Quit spaces
                break
            if key_found and list_of_lines[-1].endswith(")"):  # Only for depends and makedepends
                list_of_lines[-1] = list_of_lines[-1].strip(")")
                break
            if key_found and not line.endswith(")") and not line.startswith(f"{key}="):
                if " " in line and ":" not in line:
                    for package in line.split():
                        list_of_lines.append(package)
                else:
                    list_of_lines.append(line.split("#")[0].strip())
            if key_found and line.endswith(")"):
                list_of_lines += line.rstrip(")").strip().split()
                break
        list_of_lines = list(filter(None, list_of_lines))
        if list_of_lines:
            return self.processvar(list_of_lines)
        raise ParserKeyError(f"{key} not found in PKGBUILD")

    def get_base(self, key: str):
        """Basic function to obtain simple values."""
        for line in self.lines:
            if line.startswith(f"{key}="):
                # line example: pkgdesc=("desc here") # packager's comment
                # line.split("=")[1] example: ("desc here") # packager's comment
                # line.split("=")[1].split("#")[0].lstrip("(").rstrip(")") example: "package info"
                return self.processvar(remove_quotes(
                    line.split("=")[1].split("#")[0].lstrip("(").rstrip(")")
                ))
        raise ParserKeyError(f"{key} not found in PKGBUILD")

    def replacevar(self, var: str) -> str:
        names: list[str] = []
        for func in dir(self):
            if func.startswith("get_") and func != "get_base":
                names.append(func.lstrip("get_"))
                names.append(func.lstrip("get"))
        vars_to_replace = {}
        for name in names:
            if name == "arch" and ("$arch" in var or "${arch}" in var):
                archs = self.multiline("arch")
                if len(archs) > 1 and machine() in archs:
                    vars_to_replace["arch"] = machine()
                else:
                    vars_to_replace["arch"] = archs[0]
            elif f"${name}" in var or "${"+name+"}" in var:
                vars_to_replace[name] = self.get_base(name)
        for name, new_var in vars_to_replace.items():
            var = var.replace(f"${name}", new_var).replace("${"+name+"}", new_var)
        return var

    def processvar(self, var_returned: str | list[str]) -> str | list[str]:
        if isinstance(var_returned, list):
            new_var = []
            for var_parsed in var_returned:
                new_var.append(self.replacevar(var_parsed))
        else:
            new_var = self.replacevar(var_returned)
        return new_var
