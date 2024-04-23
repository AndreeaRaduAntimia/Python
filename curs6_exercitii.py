"""
Cerinte:

Clasa pisica
Atribute:
- culoare
- rasa
- varsta


Metode:
- miauna
- alearga
- zgarie
- se joaca
- toarce
"""

class Pisica:
    culoare = None
    rasa = None
    varsta = None
    lungime_blana = "3cm"

    def __init__(self, rasa):
        self.rasa = rasa

    def miauna(self):
        print("Miauuuuuu")

    def alearga(self):
        print("Am alergat de mi-au sarit capacele")

    def zgarie(self):
        print("Hrrrrrrrrrstiii")

    def toarce(self):
        print("Mrrrrrrrrrrrr")

    def seteaza_lungime_blana_noua(self):
        if self.rasa == "sfinx":
            self.lungime_blana = "0cm"

pisica_sfinx = Pisica("sfinx")
pisica_sfinx.culoare = "Roz"
print(pisica_sfinx.culoare)

pisica_sfinx.seteaza_lungime_blana_noua()
print(pisica_sfinx.lungime_blana)

