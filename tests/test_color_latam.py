import unittest

import color_latam


class FuncionesDeColorTest(unittest.TestCase):
    def test_funciones_historicas_conservan_su_salida(self):
        casos = {
            color_latam.rojo: "\033[91mtexto\033[0m",
            color_latam.verde: "\033[92mtexto\033[0m",
            color_latam.amarillo: "\033[93mtexto\033[0m",
            color_latam.azul: "\033[94mtexto\033[0m",
            color_latam.negro: "\033[0;30mtexto\033[0m",
            color_latam.magenta: "\033[0;35mtexto\033[0m",
        }

        for funcion, esperado in casos.items():
            with self.subTest(funcion=funcion.__name__):
                self.assertEqual(funcion("texto"), esperado)

    def test_nuevos_colores(self):
        self.assertEqual(color_latam.cian("texto"), "\033[36mtexto\033[0m")
        self.assertEqual(color_latam.blanco("texto"), "\033[37mtexto\033[0m")

    def test_acepta_objetos_que_no_son_cadenas(self):
        self.assertEqual(color_latam.rojo(42), "\033[91m42\033[0m")


class ColorearTest(unittest.TestCase):
    def test_normaliza_el_nombre(self):
        self.assertEqual(color_latam.colorear("ok", " VERDE "), "\033[92mok\033[0m")

    def test_combina_estilos(self):
        resultado = color_latam.colorear("aviso", "amarillo", negrita=True, subrayado=True)
        self.assertEqual(resultado, "\033[1;4;93maviso\033[0m")

    def test_rechaza_color_desconocido(self):
        with self.assertRaisesRegex(ValueError, "color desconocido"):
            color_latam.colorear("texto", "naranja")

    def test_rechaza_un_nombre_que_no_sea_cadena(self):
        with self.assertRaisesRegex(TypeError, "color debe ser una cadena"):
            color_latam.colorear("texto", 1)  # type: ignore[arg-type]


class PaqueteTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(color_latam.__version__, "0.1.0")

    def test_api_publica(self):
        for nombre in color_latam.__all__:
            with self.subTest(nombre=nombre):
                self.assertTrue(hasattr(color_latam, nombre))


if __name__ == "__main__":
    unittest.main()
