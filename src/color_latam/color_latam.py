"""Utilidades para aplicar colores ANSI a texto de terminal."""

import re
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


def _validar_componente(nombre: str, valor: object) -> int:
    """Valida y devuelve un componente RGB."""
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(f"{nombre} debe ser un número entero")
    if not 0 <= valor <= 255:
        raise ValueError(f"{nombre} debe estar entre 0 y 255")
    return valor


def color_rgb(
    texto: object,
    rojo: int,
    verde: int,
    azul: int,
    *,
    fondo: bool = False,
    negrita: bool = False,
    subrayado: bool = False,
) -> str:
    """Devuelve texto con un color RGB de 24 bits.

    Los componentes ``rojo``, ``verde`` y ``azul`` deben ser enteros entre
    0 y 255. Con ``fondo=True``, el color se aplica al fondo en vez del texto.
    """
    componentes = (
        _validar_componente("rojo", rojo),
        _validar_componente("verde", verde),
        _validar_componente("azul", azul),
    )

    codigos = []
    if negrita:
        codigos.append("1")
    if subrayado:
        codigos.append("4")

    destino = "48" if fondo else "38"
    codigos.extend([destino, "2", *(str(componente) for componente in componentes)])
    return f"\033[{';'.join(codigos)}m{texto}{RESET}"


def color_hex(
    texto: object,
    color: str,
    *,
    fondo: bool = False,
    negrita: bool = False,
    subrayado: bool = False,
) -> str:
    """Devuelve texto con un color hexadecimal de tres o seis dígitos.

    Acepta formatos como ``#ff8800``, ``ff8800``, ``#f80`` y ``f80``.
    """
    if not isinstance(color, str):
        raise TypeError("color debe ser una cadena hexadecimal")

    coincidencia = re.fullmatch(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", color.strip())
    if coincidencia is None:
        raise ValueError("color debe tener el formato #RGB o #RRGGBB")

    hexadecimal = coincidencia.group(1)
    if len(hexadecimal) == 3:
        hexadecimal = "".join(digito * 2 for digito in hexadecimal)

    return color_rgb(
        texto,
        int(hexadecimal[0:2], 16),
        int(hexadecimal[2:4], 16),
        int(hexadecimal[4:6], 16),
        fondo=fondo,
        negrita=negrita,
        subrayado=subrayado,
    )


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
