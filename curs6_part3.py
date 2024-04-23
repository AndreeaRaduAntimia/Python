class Angajat:
    nume = None
    salariu = 10000
    functia = "Manager"
    program_lucru = "Part_time"

    def __init__(self, nume):
        self.nume = nume

    def afiseaza_nume(self):
        print(self.nume)

    def mareste_salariul(self):
        self.salariu = self.salariu + 1000
        print(self.salariu)


angajat1 = Angajat("Popescu")
angajat1.mareste_salariul()
angajat1.afiseaza_nume()
print(angajat1.program_lucru)

