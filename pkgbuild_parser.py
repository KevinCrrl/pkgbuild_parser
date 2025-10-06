# Licencia: MIT 2025 KevinCrrl
# Módulo sencillo para obtener datos básicos de un PKGBUILD.
# Versión 0.1.2
# Documentación en https://github.com/KevinCrrl/pkgbuild_parser/blob/main/README.md

import json

def remove_quotes(string :str) -> str:
    new_string = ""
    for char in string:
        if char != "'" and char != '"':
            new_string += char
    return new_string

class ParserFileError(Exception):
    pass

class ParserKeyError(Exception):
    pass

class Parser:
    def __init__(self, filename):
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                self.lines = [line.strip() for line in f]
        except FileNotFoundError as exc:
            raise ParserFileError(f"PKGBUILD file '{filename}' not found") from exc
        
    def get_base(self, key):
        """Función básica para obtener valores simples."""
        try:
            for line in self.lines:
                if key in line:
                    return line.split("=")[1].strip()
        except IndexError as exc:
            raise ParserKeyError(f"{key} not found in PKGBUILD") from exc
    
    def get_split(self, key):
        return self.get_base(key).split()[0]
    
    def get_strip(self, key):
        """Quita contenido inncesario de una línea más compleja con paréntesis."""
        return self.get_base(key).lstrip("(").rstrip(")")
    
    def get_split_strip(self, key):
        return self.get_base(key).split("#")[0].lstrip("()").rstrip(") ")
        
    def get_pkgname(self):
        return self.get_split("pkgname")
        
    def get_pkgver(self):
        return self.get_split("pkgver")
    
    def get_pkgrel(self):
        return self.get_split("pkgrel")
    
    def get_pkgdesc(self):
        return self.get_split_strip("pkgdesc")
    
    def get_url(self):
        return self.get_split("url")

    def get_license(self):
        return self.get_split_strip("license")

    def get_source(self):
        return self.get_split_strip("source")

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
