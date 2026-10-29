"""Utilidades para aplicar colores ANSI a texto de terminal."""

from typing import Dict

RESET = "\033[0m"

# Se conservan los códigos históricos de la biblioteca para no cambiar el
# resultado de las funciones públicas existentes.
COLORES: Dict[str, str] = {
    "negro": "0;30",
    "rojo": "91",
    "verde": "92",
    "amarillo": "93",
    "azul": "94",
    "magenta": "0;35",
    "cian": "36",
    "blanco": "37",
}


def colorear(
    texto: object,
    color: str,
    *,
    negrita: bool = False,
    subrayado: bool = False,
) -> str:
    """Devuelve ``texto`` envuelto en secuencias ANSI.

    Args:
        texto: Objeto que se convertirá a texto.
        color: Nombre del color en español. No distingue mayúsculas y
            minúsculas ni espacios alrededor del nombre.
        negrita: Activa el estilo de letra negrita.
        subrayado: Activa el estilo subrayado.

    Raises:
        TypeError: Si ``color`` no es una cadena.
        ValueError: Si el nombre del color no está disponible.
    """
    if not isinstance(color, str):
        raise TypeError("color debe ser una cadena")

    nombre = color.strip().lower()
    try:
        codigo_color = COLORES[nombre]
    except KeyError as error:
        disponibles = ", ".join(COLORES)
        raise ValueError(
            f"color desconocido: {color!r}. Colores disponibles: {disponibles}"
        ) from error

    codigos = []
    if negrita:
        codigos.append("1")
    if subrayado:
        codigos.append("4")
    if codigos and codigo_color.startswith("0;"):
        codigo_color = codigo_color[2:]
    codigos.append(codigo_color)

    return f"\033[{';'.join(codigos)}m{texto}{RESET}"


def rojo(texto: object) -> str:
    """Devuelve el texto en rojo."""
    return colorear(texto, "rojo")


def verde(texto: object) -> str:
    """Devuelve el texto en verde."""
    return colorear(texto, "verde")


def amarillo(texto: object) -> str:
    """Devuelve el texto en amarillo."""
    return colorear(texto, "amarillo")


def azul(texto: object) -> str:
    """Devuelve el texto en azul."""
    return colorear(texto, "azul")


def negro(texto: object) -> str:
    """Devuelve el texto en negro."""
    return colorear(texto, "negro")


def magenta(texto: object) -> str:
    """Devuelve el texto en magenta."""
    return colorear(texto, "magenta")


def cian(texto: object) -> str:
    """Devuelve el texto en cian."""
    return colorear(texto, "cian")


def blanco(texto: object) -> str:
    """Devuelve el texto en blanco."""
    return colorear(texto, "blanco")
