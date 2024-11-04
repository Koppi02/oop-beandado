# main.py
from rendszer.foglalasirendszer import FoglalasiRendszer


def main():
    rendszer = FoglalasiRendszer()

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Kilépés")
        valasztas = input("Kérem válasszon egy lehetőséget: ")

        if valasztas == "1":
            rendszer.legi_tarsasag.jaratok_listazasa()
        elif valasztas == "2":
            utas_nev = input("Kérem adja meg az utas nevét: ")
            jaratszam = input("Kérem adja meg a járatszámot: ")
            rendszer.jegy_foglalas(utas_nev, jaratszam)
        elif valasztas == "3":
            utas_nev = input("Kérem adja meg az utas nevét: ")
            jaratszam = input("Kérem adja meg a járatszámot: ")
            rendszer.foglalas_lemondasa(utas_nev, jaratszam)
        elif valasztas == "4":
            rendszer.foglalasok_listazasa()
        elif valasztas == "5":
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás, kérem próbálja újra")

if __name__ == "__main__":
    main()
