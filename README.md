# pkgbuild_parser

[English documentation](https://github.com/KevinCrrl/pkgbuild_parser/blob/main/ingles.md)

## Introducción

**pkgbuild_parser** es un módulo escrito en **Python** (compatible con Python 3.x) diseñado para extraer información básica de un **PKGBUILD** de Arch Linux.  
El propósito principal de este módulo es proporcionar un acceso sencillo y directo a los campos más importantes de un PKGBUILD sin depender de herramientas externas ni librerías adicionales.  

- **Versión:** 0.1.0  
- **Licencia:** MIT 2025 KevinCrrl  
- **Dependencias:** Ninguna  
- **Estilo:** Simplicidad, sin dependencias externas, fácil de usar  

Este módulo permite obtener datos como el nombre del paquete, versión, descripción, licencia, URL y archivo fuente de manera rápida y directa.  

---

## Funciones principales para el usuario

Aunque internamente el módulo tiene funciones de soporte (`get_base`, `get_split`, `get_strip`), el **usuario solo necesita usar las funciones de alto nivel**, que son claras y directas:  

| Función | Descripción |
|---------|-------------|
| `get_pkgname()` | Retorna el nombre del paquete (`pkgname`) como string. |
| `get_pkgver()` | Retorna la versión del paquete (`pkgver`) como string. |
| `get_pkgrel()` | Retorna el número de release (`pkgrel`) como string. |
| `get_pkgdesc()` | Retorna la descripción del paquete (`pkgdesc`) como string, eliminando comentarios y paréntesis innecesarios. |
| `get_url()` | Retorna la URL principal del proyecto (`url`) como string. |
| `get_license()` | Retorna la licencia del paquete (`license`) como string, sin comentarios ni paréntesis extra. |
| `get_source()` | Retorna la fuente principal (`source`) del paquete como string. |
| `get_dict_base_info()` | Retorna un diccionario con todos los campos anteriores en formato `{'pkgname': ..., 'pkgver': ..., ...}`. |
| `base_info_to_json()` | Retorna la información base en formato **JSON** con indentación y codificación UTF-8. |
| `write_base_info_to_json(json_name)` | Escribe la información base en un archivo JSON con nombre `json_name`. |

**Nota:** Las funciones internas (`get_base`, `get_split`, `get_strip`, `get_split_strip`) están pensadas para uso del módulo y **no necesitan ser usadas por el usuario**.  

---

## Instalación y uso

### Opción 1: AUR

El módulo está disponible en el AUR como **`python-pkgbuild-parser`**:

### Opción 2: Construcción manual

Si deseas construirlo manualmente:

```bash
python -m build
python -m installer --destdir=/ruta/de/instalacion dist/*.whl
```

## Uso básico

```python
import pkgbuild_parser
import sys

try:
    mi_pkgbuild = pkgbuild_parser.Parser("PKGBUILD")
except pkgbuild_parser.ParserFileError as exc:
    print(exc)
    sys.exit(1)

# Obtener datos básicos
try:
    print(mi_pkgbuild.get_pkgname())
    print(mi_pkgbuild.get_pkgver())
    print(mi_pkgbuild.get_pkgrel())
    print(mi_pkgbuild.get_pkgdesc())
    print(mi_pkgbuild.get_url())
    print(mi_pkgbuild.get_license())
    print(mi_pkgbuild.get_source())

    # Obtener un diccionario de toda la info
    info = mi_pkgbuild.get_dict_base_info()
    print(info)

    # Mostrar en formato JSON
    print(mi_pkgbuild.base_info_to_json())

    # Obtener JSON y escribirlo a archivo
    mi_pkgbuild.write_base_info_to_json("info.json")
except pkgbuild_parser.ParserKeyError as e:
    print(e)
```

## Manejo de errores

Si el archivo PKGBUILD no existe, se lanza un `ParserFileError`, que debe ser capturado para evitar que el programa falle.

También puede ocurrir que se lanza un `ParserKeyError` en caso de que la obtención de un valor del PKGBUILD falle, por ejemplo, si license no está bien declarado, y se hace get_license() se producirá dicha excepción.

## Limitaciones

- Actualmente **no soporta parsing de arrays o listas complejas**, como `depends`, `makedepends` o `provides` en múltiples líneas.  
- El objetivo del módulo es extraer únicamente **información básica** de PKGBUILD estándar.  
- Funciona mejor con PKGBUILD que siguen las normas de la **Arch Wiki**.
