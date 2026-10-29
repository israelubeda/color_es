# color-latam

[![PyPI](https://img.shields.io/pypi/v/color-latam)](https://pypi.org/project/color-latam/)
[![Python](https://img.shields.io/pypi/pyversions/color-latam)](https://pypi.org/project/color-latam/)
[![Licencia MIT](https://img.shields.io/badge/licencia-MIT-blue.svg)](https://github.com/israelubeda/color_es/blob/main/LICENSE)

Una biblioteca pequeña y sin dependencias para colorear texto en la terminal
con funciones en español. Devuelve cadenas con códigos ANSI: tú decides cuándo
y dónde imprimirlas.

## Instalación

```bash
python -m pip install color-latam
```

Requiere Python 3.8 o posterior.

## Uso rápido

```python
import color_latam

print(color_latam.rojo("Error"))
print(color_latam.verde("Operación completada"))
print(color_latam.azul("Información"))
```

Las funciones aceptan cualquier objeto que pueda convertirse a texto:

```python
from color_latam import amarillo

print(amarillo(2026))
```

## API genérica

`colorear()` permite elegir el color en tiempo de ejecución y combinarlo con
negrita o subrayado:

```python
from color_latam import colorear

mensaje = colorear("Aviso importante", "amarillo", negrita=True)
print(mensaje)

enlace = colorear("Documentación", "cian", subrayado=True)
print(enlace)
```

El nombre del color no distingue mayúsculas, minúsculas ni espacios exteriores.
Un nombre desconocido genera `ValueError` con la lista de opciones disponibles.

## Colores disponibles

| Nombre | Función directa |
| --- | --- |
| Rojo | `rojo(texto)` |
| Verde | `verde(texto)` |
| Amarillo | `amarillo(texto)` |
| Azul | `azul(texto)` |
| Negro | `negro(texto)` |
| Magenta | `magenta(texto)` |
| Cian | `cian(texto)` |
| Blanco | `blanco(texto)` |

> [!NOTE]
> La apariencia exacta depende del tema y de la compatibilidad ANSI de la
> terminal. El negro, por ejemplo, puede resultar invisible sobre un fondo
> oscuro.

## Desarrollo

Clona el repositorio e instala las herramientas opcionales:

```bash
git clone https://github.com/israelubeda/color_es.git
cd color_es
python -m pip install -e ".[dev]"
```

Ejecuta las comprobaciones:

```bash
python -m pytest
ruff check .
python -m build
twine check dist/*
```

## Publicación en PyPI

El repositorio incluye un flujo de GitHub Actions preparado para publicación
confiable, sin guardar tokens de PyPI. Antes de la primera versión:

1. Crea el proyecto o un *pending publisher* en PyPI.
2. Configura como propietario `israelubeda`, repositorio `color_es`, workflow
   `publish.yml` y entorno `pypi`.
3. Crea en GitHub un entorno llamado `pypi`.
4. Actualiza `__version__` en `src/color_latam/__init__.py`.
5. Publica una release de GitHub. El workflow construirá, comprobará y subirá
   los artefactos automáticamente.

PyPI no permite reutilizar un número de versión ya publicado.

## Licencia

Distribuido bajo la [licencia MIT](https://github.com/israelubeda/color_es/blob/main/LICENSE).
