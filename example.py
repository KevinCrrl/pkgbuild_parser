import sys
import pkgbuild_parser

print(f"pkgbuild-parser version: {pkgbuild_parser.VERSION}")

try:
    my_pkgbuild = pkgbuild_parser.Parser(extra_names=["custom_var"])
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
    print(my_pkgbuild.get_install())
    print(my_pkgbuild.get_sums("sha512"))
    print(my_pkgbuild.get_full_package_name())
    print(my_pkgbuild.get_depends())
    print(my_pkgbuild.get_makedepends())
    print(my_pkgbuild.get_optdepends())
    print(my_pkgbuild.get_options())
    print(my_pkgbuild.get_checkdepends())
    print(my_pkgbuild.get_validpgpkeys())
    print(my_pkgbuild.get_conflicts())
    print(my_pkgbuild.get_provides())
    print(my_pkgbuild.get_replaces())
    print(my_pkgbuild.get_pkgbase())
    print(my_pkgbuild.get_changelog())
    print(my_pkgbuild.get_groups())
    print(my_pkgbuild.get_noextract())
    print(my_pkgbuild.get_backup())

    # InfoDict class
    info_test = pkgbuild_parser.InfoDict(my_pkgbuild, "pkgname", "pkgver", "conflicts",
                                         multiline=True)
    print("======= SIMPLE INFO DICT =======")
    print(info_test.get_dict())
    print("======= INFO DICT AS JSON ======")
    print(info_test.to_json())
    print("Writign JSON file...")
    info_test.write_json("info_paquete.json")
    print("Done!")
except pkgbuild_parser.ParserKeyError as e:
    print(e)
