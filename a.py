class Scoala:
    nume_scoala = "Caragiale"
    nivel = "Liceu"
    nr_elevi = 350
    nr_clase = 25
    nr_prof = 40
    sali_sport = 3
    an_scolar = None

    def nume_scoala1(self, nume_scoala):
        self.nume_scoala = nume_scoala

    def nivel_scoala(self, nivel):
        self.nivel = nivel

    def numar_elevi(self, nr_elevi):
        print(f"Numarul de elevi este: {nr_elevi}")


class Elev(Scoala):
    def __init__(self, nume, nivel, clasa):
        self.nume = nume
        self.nivel = nivel
        self.clasa = clasa

    def afiseaza_mesaj(self):
        print(f"Sunt elev în scoala {self.nume_scoala}")

    def nivel_an(self, an_scolar):
        print(f"Sunt elev în anul {an_scolar}")


class Administrativ(Scoala):
    def __init__(self, nume_scoala, nivel):
        self.nume_scoala = nume_scoala
        self.nivel = nivel

    def numar_clase(self, nr_clase):
        print(f"Numarul de clase sunt {nr_clase}")

    def sali(self, sali_sport):
        print(f"Numarul de sali de sport este {sali_sport}")


admin = Administrativ(nume_scoala="Caragiale", nivel="Liceu")
admin.numar_clase(nr_clase=25)
admin.sali(sali_sport=3)

print(".........................................................")

elev1 = Elev(nume="Ionescu", nivel="Liceu", clasa="XII")
elev1.afiseaza_mesaj()
elev1.nivel_an(an_scolar="2024-2025")
