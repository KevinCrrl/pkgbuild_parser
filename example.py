import sys
import pkgbuild_parser

print(f"pkgbuild-parser version: {pkgbuild_parser.VERSION}")

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
    my_pkgbuild.write_base_info_to_json()
except pkgbuild_parser.ParserKeyError as e:
    print(e)
