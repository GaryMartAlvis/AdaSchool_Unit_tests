import unittest
import datetime

class Saludador:
    def saludar(self, nombre):
        nombre_recortado = nombre.strip()
        nombre_capitalizado = nombre_recortado.capitalize()
        hora_actual = datetime.datetime.now().time()

        if datetime.time(6, 0) <= hora_actual < datetime.time(12, 0):
            saludo = "Buenos días"
        elif datetime.time(18, 0) <= hora_actual < datetime.time(22, 0):
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"

        mensaje = f"{saludo} {nombre_capitalizado}"
        return mensaje


class PruebaSaludador(unittest.TestCase):
    def test_saludar(self):
        saludador = Saludador()
        self.assertEqual(saludador.saludar("  alice  "), "Buenas tardes Alice")
        self.assertEqual(saludador.saludar("bob"), "Buenas tardes Bob")

if __name__ == '__main__':
    unittest.main()
