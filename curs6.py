"""POO = Programare orientata pe obiecte
OOP = Object Oriented Programming

 Programare orientata pe obiecte reprezinta o modalitate prin care noi putem templetiza
atributele si comportamentul unui anumit element.

 Programarea orientata pe obiecte este prescurtata cu acronimul Exercitii_POO sau varianta in engleza
OOP  object oriented programming

 O clasa in general este unul din elementele de baza al programarii orientate pe obiecte
si reprezinta tiparul in sine

 O clasa reprezinta un tipar, dar nu va fi util pana cand nu va fi apelat
 Folosirea unei clase se poate face prin intermediul unui obiect
 Un obiect este o reprezentare efectiva a unei clase
 Crearea unui obiect se numeste instantiere, motiv pentru care, prin definitie,
        un obiect se spune ca este o instanta a unei clase
 In momentul in care cream un obiect, noi vom avea acces prin intermediul lui
        la toate atributele si metodele clasei
 O metoda este o functie definita in interiorul clasei

Constructor = Element care va fi folosit pentru instantierea obiectelor dintr-o clasa
Scopul unui constructor este de a ajuta sistemul sa instantieze obiectul dintr-o clasa
Exista doua tipuri de constructori:
a) constructor explicit care obliga utilizatorul sa populeze anumite atribute la instantierea	obiectului
                            si daca este cazul sa defineasca o regula de populare a atributelor
b) constructor implicit care este apelat automat atunci cand nu exista un constructor explicit definit

Pot sa definesc mai multi constructori in aceeasi clasa atata timp cat vor avea un numar diferit de parametri
                    (method overloading) - polimorfism -> In python nu e posibila definirea mai multor constructori


Exemplu: Clasa masina
Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca

O masina de exemplu poate sa aiba urmatoarele atribute:
 culoare
 viteza
 an_fabricatie
 marca
 model
 capacitate_rezervor
 tip_combustibil
 tractiune
 serie_sasiu
 cutie_viteze
 numar_inmatriculare

O masina poate sa faca urmatoarele actiuni
 pornire de pe loc
 oprire
 accelerare
 franare
 consum_instant
 revizie_tehnica (daca masina este in stare buna, trece revizia tehnica)
 schimbare_directie
 vopsire_masina
"""

"""
Definirea clasei se face prin intermediul keywordului "class"
De regula, prin conventie, numele unei clase va incepe cu litera mare si va fi scris in format
        camelCase sau snake_case (de regula snake_case in python)
La fel ca la structurile alternative (IF) si cele repetitive (WHILE, FOR), corpul unei clase este definit
        de indentarea codului, adica lasarea unui spatiu intre marginea fisierului si cod

Constructor = un agent care este responsabil cu crearea obiectului
In orice limbaj de programare Exercitii_POO exista un constructor implicit si un constructor explicit

Constructorul explicit este cel care se defineste de catre dezvoltator in cod
Constructorul implicit este cel care se apeleaza automat de python atunci cand constructorul explicit nu este definit

Constructorul este o functie/metoda specifica unei clase care are rolul de a crea obiectul in sine
Constructorul se defineste cu numele __init__ si intre paranteze se vor specifica atributele
        care vrem sa existe in mod obligatoriu la crearea obiectului
        Daca nu se specifica niciun parametru, atunci toate atributele vor fi optionale

In general, intr-o clasa, atunci cand vrem sa accesam elemente definite in interiorul clasei 
        fie ele atribute sau metode, ele trebuie accesate cu elementul "self."
"""


class Masina:
    # fields/attribute/proprietati
    model = None
    culoare = "Galben"  # Negru
    marca = None
    viteza_max = 0
    an_fabricatie = 0
    capacitate_rezervor = 40
    tip_combustibil = "motorina"
    tractiune = "fata"
    serie_sasiu = None
    cutie_viteze = "manuala"
    numar_inmatriculare = None
    consum_viteza_max = None
    consum_interactiv = None

    def __init__(self, marca, model, culoare):  # self reprezinta un placeholder pentru viitorul nume al obiectului care se va instantia
        # marca, model si culoare reprezinta ARGUMENTELE constructorului si ele vor fi considerate obligatorii la momentul instantierii obiectului
        self.model = model  # aici vom atribui atributelor clasei valorile date ca si PARAMETRU in interiorul constructorului
        # in stanga egalului vor fi intotdeauna atributele clasei care vor trebui initializate, iar in dreapta argumentele
        # constructorului care vor fi stocate in atributele clasei
        self.culoare = culoare
        self.marca = marca
        while isinstance(model, (int, float)):  # verific daca inputul de la utilizator este un string
            model = input(
                'Invalid value, please try again.')  # daca nu este string, rog utilizatorul sa introduca o noua valoare
        if culoare == 'orange':  # verificam daca culoarea data ca si argument in constructor este orange
            self.culoare = 'portocaliu'  # daca este orange, o schimbam in portocaliu pentru ca nu avem culoarea orange in baza de date
        if marca == "BMW":
            self.marca = "Mercedes"

    # metode
    def accelerare(self,
                   viteza):  # argumentul self este obligatoriu pentru ca tine loc de numele obiectului care inca nu este definit
        # argumentul viteza este dat ca si parametru si care va fi instantiat diferit in functie de obiectul nostru
        return f'Trebuie sa acceleram cu {viteza} de km'  # avem nevoie de return in cazul asta specific pentru
        # ca mai jos am folosit in print rezultatul functiei

    def vopsire(self, colour):
        self.culoare = colour

    def start_masina(self):
        print("Start masina")

    def calcul_consum_interactiv(self, viteza):
        for viteza in range(100, 190):
            if 180 >= viteza > 160:
                self.consum_interactiv = 10
            elif 160 >= viteza > 120:
                self.consum_interactiv = 7
            elif 120 >= viteza > 100:
                self.consum_interactiv = 6
            else:
                self.consum_interactiv = 5
        return self.consum_interactiv

    def calcul_viteza_max(self):
        if 180 >= self.viteza_max > 160:
            self.consum_viteza_max = 10
        elif 160 >= self.viteza_max > 120:
            self.consum_viteza_max = 7
        elif 120 >= self.viteza_max > 100:
            self.consum_viteza_max = 6
        else:
            self.consum_viteza_max = 5
        return self.consum_viteza_max

"""
instantierea unui obiect se face pe baza numelui clasei
Putem modifica alti parametri, sau chiar pe cei definiti prin constructor, dupa instantiere
IMPORTANT:
Orice atribut sau functie din interiorul clasei se poate accesa DOAR prin intermediul obiectului
"""
instanta_masina_bmw = Masina("BMW", "X5","orange")  # Am instantiat un obiect al clasei Masina numit instanta_masina_bmw
print(instanta_masina_bmw.culoare)
print(instanta_masina_bmw.marca)
instanta_masina_bmw.culoare = "Albastru"
print("------------")

print(instanta_masina_bmw.viteza_max)
instanta_masina_bmw.viteza_max = 120
print(instanta_masina_bmw.viteza_max)
print(instanta_masina_bmw.an_fabricatie)
print("------------")


instanta_masina_volkswagen = Masina("Dacia", "Logan", "negru")
instanta_masina_volkswagen.viteza_max = 180
print("------------")

instanta_masina_golf = Masina("Volkswagen", "Golf", "Albastru")
instanta_masina_golf.viteza_max = 180
print("------------")

# Nota: Putem sa consideram ca numele clasei este tipul de data al unui obiect
print(f"Culoarea pentru prima masina este {instanta_masina_bmw.culoare}")
print(type(instanta_masina_bmw))
print("------------")

instanta_masina_golf.start_masina()


if __name__ == "__main__":
    instanta_masina4 = Masina("Dacia", "Spring", "Negru")
    instanta_masina5 = Masina("BMW", "X3", "orange")
    print(instanta_masina4.model, instanta_masina4.culoare)
    print(instanta_masina5.model, instanta_masina5.culoare)

    print(instanta_masina_bmw.viteza_max)

