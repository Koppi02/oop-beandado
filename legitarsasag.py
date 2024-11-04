# foglalasi_rendszer/legitarsasag.py
from .jarat import Jarat


class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        if not self.jaratok:
            print("Nincsenek elérhető járatok.")
            return

        print("Elérhető járatok:")
        for jarat in self.jaratok:
            print(
                f"Járatszám: {jarat.jaratszam}, Célállomás: {jarat.celallomas}, Ár: {jarat.jegyar}, Típus: {jarat.jarat_tipusa()}")
