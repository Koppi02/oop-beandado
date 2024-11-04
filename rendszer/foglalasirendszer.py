
from .legitarsasag import LegiTarsasag
from .jegyfoglalas import JegyFoglalas
from .jarat import BelfoldiJarat, NemzetkoziJarat

class FoglalasiRendszer:
    def __init__(self):
        self.legi_tarsasag = LegiTarsasag("RepuloTarsasag")
        self.foglalasok = []
        self.elore_feltoltes()

    def elore_feltoltes(self):

        belfoldi_jarat1 = BelfoldiJarat("BF100", "Budapest", 5000)
        belfoldi_jarat2 = BelfoldiJarat("BF101", "Debrecen", 4000)
        nemzetkozi_jarat1 = NemzetkoziJarat("N200", "Barcelona", 30000)

        self.legi_tarsasag.jarat_hozzaadas(belfoldi_jarat1)
        self.legi_tarsasag.jarat_hozzaadas(belfoldi_jarat2)
        self.legi_tarsasag.jarat_hozzaadas(nemzetkozi_jarat1)

        self.foglalasok.append(JegyFoglalas("Kovácsik Anna", belfoldi_jarat1))
        self.foglalasok.append(JegyFoglalas("Bartolák Aliz", nemzetkozi_jarat1))
        self.foglalasok.append(JegyFoglalas("Renkecz Máté", belfoldi_jarat2))
        self.foglalasok.append(JegyFoglalas("Magda László", nemzetkozi_jarat1))
        self.foglalasok.append(JegyFoglalas("Sallai Gergely", belfoldi_jarat1))
        self.foglalasok.append(JegyFoglalas("Sörös Ármin", belfoldi_jarat2))

    def jegy_foglalas(self, utas_nev, jaratszam):
        jarat = next((j for j in self.legi_tarsasag.jaratok if j.jaratszam == jaratszam), None)
        if jarat:
            foglalas = JegyFoglalas(utas_nev, jarat)
            self.foglalasok.append(foglalas)
            print(f"Foglalás sikeres! Foglalási összeg: {foglalas.foglalasi_osszeg()} Ft")
        else:
            print("A megadott járatszám nem létezik.")

    def foglalas_lemondasa(self, utas_nev, jaratszam):
        foglalas = next((f for f in self.foglalasok if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam), None)
        if foglalas:
            self.foglalasok.remove(foglalas)
            print("A foglalás sikeresen le lett mondva.")
        else:
            print("A megadott foglalás nem található.")

    def foglalasok_listazasa(self):
        if self.foglalasok:
            print("Aktuális foglalások:")
            for foglalas in self.foglalasok:
                print(f"Utas: {foglalas.utas_nev}, Járat: {foglalas.jarat.jaratszam}, Célállomás: {foglalas.jarat.celallomas}")
        else:
            print("Nincsenek aktuális foglalások.")
