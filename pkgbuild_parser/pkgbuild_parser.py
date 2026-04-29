#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Python module to extract information directly from PKGBUILD files (not .SRCINFO)
# Version 1.2.1
# Docs: https://github.com/KevinCrrl/pkgbuild_parser/blob/main/README.md

import json
from pkgbuild_parser.parser_core import ParserCore, ParserKeyError


class Parser(ParserCore):
    def get_pkgname(self):
        return self.get_base("pkgname")

    def get_pkgver(self):
        return self.get_base("pkgver")

    def get_pkgrel(self):
        return self.get_base("pkgrel")

    def get_pkgdesc(self):
        return self.get_base("pkgdesc")

    def get_arch(self) -> list[str]:
        return self.multiline("arch")

    def get_url(self):
        return self.get_base("url")

    def get_license(self) -> list[str]:
        return self.multiline("license")

    def get_source(self) -> list[str]:
        return self.multiline("source")

    def get_epoch(self):
        return self.get_base("epoch")

    def get_full_version(self) -> str:
        version = f"{self.get_pkgver()}-{self.get_pkgrel()}"
        try:
            return f"{self.get_epoch()}:{version}"
        except ParserKeyError:
            return f"{version}"

    def get_full_package_name(self) -> str:
        name = self.get_pkgname()
        version = f"{self.get_pkgver()}-{self.get_pkgrel()}"
        try:
            return f"{self.get_epoch()}:{name}-{version}"
        except ParserKeyError:
            return f"{name}-{version}"

    def get_depends(self) -> list[str]:
        return self.multiline("depends")

    def get_makedepends(self) -> list[str]:
        return self.multiline("makedepends")

    def get_optdepends(self) -> dict[str, str]:
        opt_dict: dict[str, str] = {}
        for optdepend in self.multiline("optdepends"):
            optdepend = optdepend.split(":")
            opt_dict[optdepend[0]] = optdepend[1].strip()
        return opt_dict

    def get_options(self) -> list[str]:
        return self.multiline("options")

    def get_checkdepends(self) -> list[str]:
        return self.multiline("checkdepends")

    def get_sums(self, algorithm: str) -> list[str]:
        return self.multiline(f"{algorithm.strip()}sums")

    def get_validpgpkeys(self) -> list[str]:
        return self.multiline("validpgpkeys")

    def get_conflicts(self) -> list[str]:
        return self.multiline("conflicts")

    def get_provides(self) -> list[str]:
        return self.multiline("provides")

    def get_replaces(self) -> list[str]:
        return self.multiline("replaces")

    def get_pkgbase(self):
        return self.get_base("pkgbase")


class InfoDict():
    def __init__(self, parser: Parser, *info_to_get: str, multiline: bool = False,
                 ignore_errors: bool = False):
        def loop():
            if multiline:
                self.info_dict[info] = parser.multiline(info)
            else:
                self.info_dict[info] = parser.get_base(info)

        self.parser = parser
        self.info_dict = {}
        for info in info_to_get:
            if ignore_errors:
                try:
                    loop()
                except ParserKeyError:
                    pass
            else:
                loop()

    def get_dict(self) -> dict[str, str | list[str]]:
        return self.info_dict

    def to_json(self) -> str:
        return json.dumps(self.get_dict(),
                          ensure_ascii=False, indent=4)

    def write_json(self, json_name: str = "InfoDict.json") -> None:
        with open(json_name, 'w', encoding="utf-8") as f:
            f.write(self.to_json())
