class Angajat:
    salariu = 1000
    nume = ""

    def seteaza_nume(self, nume):
        self.nume = nume

    def afiseaza_nume(self):
        print(self.nume)

    def afiseaza_mesaj(self):
        print("Mesaj clasa Angajat")

angajat1 = Angajat()

angajat1.seteaza_nume("Popescu")
angajat1.afiseaza_nume()
print(Angajat.nume)

class Contabil(Angajat):
    salariu = 500

    def afiseaza_mesaj(self):
        print("Mesaj clasa Contabil")

    def seteaza_salariu(self, salariu):
        self.salariu = salariu

angajat2 = Contabil()
angajat2.afiseaza_mesaj()
angajat2.afiseaza_nume()
print(angajat2.salariu)
angajat2.seteaza_nume("Cartof")
print(angajat2.nume)
print("------------------")

angajat3 = Contabil()
angajat3.seteaza_nume("Tudose")
print(angajat3.nume)
print(angajat3.salariu)
angajat3.seteaza_salariu(750)
print(angajat3.salariu)

class Junior(Contabil):
    salariu = 400

    def seteaza_salariu(self, salariu):
        self.salariu = salariu

j1 = Junior()
print(j1.salariu)
