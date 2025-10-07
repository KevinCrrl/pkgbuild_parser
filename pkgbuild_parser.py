# Licencia: MIT 2025 KevinCrrl
# Módulo sencillo para obtener datos básicos de un PKGBUILD.
# Versión 0.2.0
# Documentación en https://github.com/KevinCrrl/pkgbuild_parser/blob/main/README.md

import json

class ParserFileError(Exception):
    pass

class ParserKeyError(Exception):
    pass

class ParserNoneTypeError(Exception):
    pass

def remove_quotes(string :str) -> str:
    new_string = ""
    for char in string:
        if char != "'" and char != '"':
            new_string += char
    return new_string
    
class Parser:
    def __init__(self, filename: str):
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                self.lines = [line.strip() for line in f]
        except FileNotFoundError as exc:
            raise ParserFileError(f"PKGBUILD file '{filename}' not found") from exc

    def get_base(self, key: str):
        "Basic function to obtain simple values."
        try:
            for line in self.lines:
                if key in line:
                    # line example: pkgdesc=("desc here") # packager's comment
                    # line.split("=")[1].strip() example: ("desc here") # packager's comment
                    # line.split("=")[1].strip().split("#")[0].lstrip("(").rstrip(") ") example: "package info"
                    return line.split("=")[1].strip().split("#")[0].lstrip("(").rstrip(") ")
        except IndexError as exc:
            raise ParserKeyError(f"{key} not found in PKGBUILD") from exc
        except AttributeError as exc:
            raise ParserNoneTypeError(f"'NoneType' returned when trying to get {key}") from exc

    def get_pkgname(self):
        return self.get_base("pkgname")

    def get_pkgver(self):
        return self.get_base("pkgver")

    def get_pkgrel(self):
        return self.get_base("pkgrel")

    def get_pkgdesc(self):
        return self.get_base("pkgdesc")

    def get_url(self):
        return self.get_base("url")

    def get_license(self):
        return self.get_base("license")

    def get_source(self):
        return self.get_base("source")

    def get_dict_base_info(self):
        return {"pkgname": self.get_pkgname(),
                "pkgver": self.get_pkgver(),
                "pkgrel": self.get_pkgrel(),
                "pkgdesc": self.get_pkgdesc(),
                "url": self.get_url(),
                "license": self.get_license(),
                "source": self.get_source()}

    def base_info_to_json(self):
        return json.dumps(self.get_dict_base_info(), ensure_ascii=False, indent=4)

    def write_base_info_to_json(self, json_name):
        with open(json_name, 'w', encoding="utf-8") as f:
            f.write(self.base_info_to_json())

    def get_dict_base_info_without_quotes(self):
        return {"pkgname": remove_quotes(self.get_pkgname()),
                "pkgver": remove_quotes(self.get_pkgver()),
                "pkgdesc": remove_quotes(self.get_pkgdesc()),
                "url": remove_quotes(self.get_url()),
                "license": remove_quotes(self.get_license()),
                "source": remove_quotes(self.get_source())}

    def base_info_to_json_without_quotes(self):
        return json.dumps(self.get_dict_base_info_without_quotes(), ensure_ascii=False, indent=4)

    def write_base_info_to_json_without_quotes(self, json_name):
        with open(json_name, 'w', encoding="utf-8") as f:
            f.write(self.base_info_to_json_without_quotes())

    def get_epoch(self):
        epoch = self.get_base("epoch")
        if not epoch is None:
            return epoch
        else:
            raise ParserNoneTypeError("'NoneType' returned when trying to get epoch")

    def get_full_package_name(self):
        name = remove_quotes(self.get_pkgname())
        version = f"{remove_quotes(self.get_pkgver())}-{remove_quotes(self.get_pkgrel())}"
        try:
            return f"{name}-{remove_quotes(self.get_epoch())}:{version}"
        except ParserNoneTypeError:
            return f"{name}-{version}"

    def get_list_source(self):
        return remove_quotes(self.get_source()).split()
