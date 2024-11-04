# foglalasi_rendszer/jegyfoglalas.py
from .jarat import Jarat

class JegyFoglalas:
    def __init__(self, utas_nev, jarat):
        self.utas_nev = utas_nev
        self.jarat = jarat

    def foglalasi_osszeg(self):
        return self.jarat.jegyar
