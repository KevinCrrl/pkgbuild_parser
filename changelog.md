# Changelog

## Versión 0.3.0 (2025-10-09)

### Nuevas características

- **Soporte para arrays multilínea**: Se ha añadido la función `multiline(key)` para extraer valores que se extienden por varias líneas en el PKGBUILD, como `source`, `depends`, `makedepends` y `optdepends`.
- **Nuevas funciones para el usuario**:
  - `get_arch()`: Obtiene la arquitectura del paquete.
  - `get_depends()`: Obtiene la lista de dependencias.
  - `get_makedepends()`: Obtiene la lista de dependencias de compilación.
  - `get_optdepends()`: Obtiene la lista de dependencias opcionales.
  - `get_dict_optdepends()`: Convierte las dependencias opcionales en un diccionario.
  - `get_list_arch()`: Obtiene la lista de arquitecturas.

### Mejoras

- **`get_source()` mejorado**: Ahora devuelve una lista de fuentes, gracias a la nueva capacidad de `multiline()`.
- **`get_dict_base_info()` actualizado**: El diccionario de información base ahora incluye el campo `arch`.
- **Refactorización de `get_dict_base_info_without_quotes()`**: La función ha sido simplificada para mayor claridad y eficiencia.

### Cambios deprecados

- **`get_list_source()` eliminado**: Esta función ha sido eliminada, ya que `get_source()` ahora devuelve una lista directamente.

### Correcciones

- **Manejo de `epoch`**: Se ha mejorado la lógica para manejar casos donde `epoch` no está presente, lanzando un `ParserNoneTypeError` de manera más consistente.
