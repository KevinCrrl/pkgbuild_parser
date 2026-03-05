# Licencia: MIT 2025-2026 KevinCrrl

import warnings

warnings.simplefilter("always", DeprecationWarning)


class ParserFileError(Exception):
    pass


class ParserKeyError(Exception):
    pass


class ParserNoneTypeError(Exception):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "ParserNoneTypeError is deprecated, use ParserKeyError instead.",
            DeprecationWarning,
            stacklevel=2
        )
        super().__init__(*args, **kwargs)


def remove_quotes(string) -> list[str] | str:
    if isinstance(string, list):
        return string
    new_string = ""
    for char in string:
        if char not in ("'", '"'):
            new_string += char
    return new_string


class ParserCore:
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
            line: str = remove_quotes(line.split("#")[
                                          0].strip())  # new line example: optdepends=(one_package: one_desc) or optdepends=(package: desc
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
                list_of_lines.append(line.rstrip(")").strip())
                break
        list_of_lines = list(filter(None, list_of_lines))
        if list_of_lines:
            return list_of_lines
        raise ParserKeyError(f"{key} not found in PKGBUILD")

    def get_base(self, key: str):
        """Basic function to obtain simple values."""
        for line in self.lines:
            if line.startswith(f"{key}="):
                # line example: pkgdesc=("desc here") # packager's comment
                # line.split("=")[1] example: ("desc here") # packager's comment
                # line.split("=")[1].split("#")[0].lstrip("(").rstrip(")") example: "package info"
                return remove_quotes(
                    line.split("=")[1].split("#")[0].lstrip("(").rstrip(")")
                )
        raise ParserKeyError(f"{key} not found in PKGBUILD")
