## [unreleased]

### 💼 Other

- Update README.md
- Fix README.md
- CI: replace flake8 by ruff and replace archlinux container by alpine
- Pyproject.toml: add ruff ignore
- Initial support for variables with architecture (not complete)
- Add get_by_arch support to other variables
- Add auto option to arch argument
## [2.3.0] - 2026-08-12

### 💼 Other

- Update example and changelog
- Add cache option and clear legacy code; migrating to shlex.split
- Add custom variables to replacevar using the Parser class
- Update changelog and update version to 2.3.0
- Update README.md and create version 2.3.0
## [2.2.0] - 2026-08-02

### 💼 Other

- Add general CoC
- Add CONTRIBUTING.md file
- Add support for multiple variables
- Version 2.2.0
## [2.1.0] - 2026-06-13

### 💼 Other

- Version 2.1.0
## [2.0.0] - 2026-04-29

### 🐛 Bug Fixes

- Fix parser_core.py multiline function and using multiline for get_pkgbase function

### 💼 Other

- Creating example.py and update README
- [BREAKING] Deleting deprecated exception
- [BREAKING] replacing sha256sums and sha512sums functions by get_sums(algorithm) function
- [BREAKING] Creating InfoDict class and removing multiple functions from Parser class
- Removing code that deletes keys for unknown vars.
- Adding ignore_errors option to InfoDict class
- Update README
- Version 2.0.0; See the changelog.md
## [1.2.1] - 2026-03-31

### 💼 Other

- Version 1.2.1: Fix parser_core.py arch detection in replacevar()
- Fix pyproject.toml
## [1.2.0] - 2026-03-30

### 🐛 Bug Fixes

- Fix deprecated version

### 💼 Other

- Support for replace known Bash vars and migrating to MPL-2.0 License
- Adding workflow for flake8
- Fix workflow
- Update README
- Parser_core.py: fix replacevar() bugs
- Update changelog and README
## [1.1.0] - 2026-03-05

### 💼 Other

- Actualizando docs
- Quitando docs de repositorio temporal de aprendizaje
- Moviendo documentación en español a sitio web y dejando inglés como README.md
- Version 1.1.0, Cambios en el changelog.md
## [1.0.1] - 2025-12-22

### 💼 Other

- Version 1.0.1: Correción de error de parseo

- Corregido error en la función principal multiline que hacía un mal
  parseo de listas y strings lo que producía resultados separados y
altamente incorrectos.
- Corregido error en la función principal multiline que hacía continuar
  a la función cuando el parseo se debía terminar, lo que producía
resultados repetidos o altamente incorrectos.
- Actualizando changelog
## [1.0.0] - 2025-12-05

### 💼 Other

- Versión 1.0.0:

- Mejor estabilidad y soporte más amplio en las funciones que usan multiline()
- Uso de remove_quotes() en todas las funciones que usan get_base()
- Eliminación de funciones innecesarias (*_without_quotes)
- Nuevas funciones para obtener más datos de un PKGBUILD.

Más información sobre los cambios en el archivo changelog.md
## [0.4.1] - 2025-11-19

### 💼 Other

- Versión 0.4.1

Mejora en la función multiline de la clase ParserCore para evitar
errores en distintos casos de PKGBUILD, esta mejora beneficia a todas
las funciones que usan la función multiline.
## [0.4.0] - 2025-11-11

### 💼 Other

- Nueva versión, cambios disponibles en cangelog.md
## [0.3.1] - 2025-10-11

### 💼 Other

- Versión 0.3.1 cambios visibles en changelog
## [0.3.0] - 2025-10-09

### 💼 Other

- Versión 0.3.0 con cambios visibles en changelog.md
## [0.2.0] - 2025-10-07

### 💼 Other

- Nueva versión 0.2.0 con nuevas funciones y cambios disponibles en el README
## [0.1.2] - 2025-10-06

### 💼 Other

- Función para remover comillas simples y dobles que ayuda a removerlas de los valores que retorna el PKGBUILD
## [0.1.1] - 2025-10-06

### 💼 Other

- Arreglo a setup.py
## [0.1.0] - 2025-10-06

### 💼 Other

- Añadiendo archivos para la primera versión
