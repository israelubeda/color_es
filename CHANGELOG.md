# Historial de cambios

Todos los cambios relevantes de este proyecto se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y las versiones siguen [Semantic Versioning](https://semver.org/lang/es/).

## [Sin publicar]

## [0.1.1] - 2026-10-29

### Añadido

- Colores personalizados de 24 bits con `color_rgb()`.
- Colores hexadecimales largos y cortos con `color_hex()`.
- Soporte para aplicar colores personalizados al fondo y combinarlos con
  negrita o subrayado.
- Validación descriptiva de componentes RGB y códigos hexadecimales.

## [0.1.0] - 2026-10-29

### Añadido

- Función genérica `colorear()` con estilos de negrita y subrayado.
- Colores cian y blanco.
- Tipado de la API pública y marcador `py.typed`.
- Pruebas automatizadas y flujos de integración y publicación continua.

### Cambiado

- Documentación, metadatos de PyPI y licencia corregidos.
- Estructura de empaquetado reproducible con Hatchling.

### Compatibilidad

- Se conservan las funciones públicas de la versión 0.0.2.

[Sin publicar]: https://github.com/israelubeda/color_es/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/israelubeda/color_es/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/israelubeda/color_es/compare/v0.0.2...v0.1.0
