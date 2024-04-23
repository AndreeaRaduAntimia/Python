"""
O functie este o modalitate prin care putem sa economisim cod.
O functie putem sa o definim o singura data si apoi sa facem ceea ce se numeste
    apelare a functiei
Apelarea functiei inseamna trimiterea sistemului catre adresa de memorie care poarta
    numele functiei
Definirea unei functii se poate face pe baza keyword-ului def
O functie POATE sa aiba parametri, dar nu este obligatoriu sa aiba
Chiar daca functia NU are parametri, parantezele de dupa numele functiei sunt
    obligatorii atat la definire cat si la apelare
Un parametru reprezinta o informatie de care functia are nevoie din exterior
    pentru a putea executa toate instructiunile
Putem alege sa parametrizam o functie atunci cand vrem ca functia noastra
    sa poata sa fie rulata pentru o plaja mai mare de valori
    ex: suma intre doua numere, putem avea alte doua numere la fiecare rulara
O functie POATE sa aiba optiune de return, dar nu este obligatoriu sa aiba
Vom alege sa punem optiune de return pe functie atunci cand vrem sa salvam rezultatul
    acelei functii intr-o variabila sau sa trimitem acel rezultat catre un sistem extern
"""

# def salut():
#     print('Hai salut')
#     print("---------------")
#
# salut()

"""
def - keyword ul care anunta inceputul definirii unei functii
salut - numele functiei, care este dat de catre user si care poate sa fie orice  (free text)
            in general, numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care PUTEM sa specificam parametri. In cazul functiei salut
            nu avem parametri, motiv pentru care parantezele sunt goale
: - reprezentant al inceputului corpului functiei, adica locul in care vom incepe sa descriem
            actiunea pe care trebuie sa o faca functia
print('Hai salut') - actiunea pe care trebuie sa o faca functia
Corpul unei functii va fi definit la fel ca la structurile alternative (if) si repetitive  (while, for)
            prin intermediul indentarii (adica spatiul lasat liber de la marginea fisierul python
            pana la inceputul liniei de cod)
"""

# salut()  # daca nu punem parantezele, nu se va executa corpul functiei, pentru ca nu va fi vazuta
# # ca o functie
# print("------------")
# """
# Apelarea functiei simple, fara parametri se va face specificand numele functiei
#         urmat de doua paranteze.
# Daca nu avem parametri in functie, atunci vom lasa parantezele goale
# In momentul in care codul va fi executat, sistemul va cauta adresa de memorie care poarta numele
#         de say_hi, va citi codul stocat la acea adresa de memorie si il va executa
# """
# x = salut()  # aici se va executa metoda salut chiar daca se va salva in variabila x
#
# print(x)  # se va printa pe ecran keyword-ul None, pentru ca functia nu are setata posibilitatea
# # de a trimite spre exterior valorile
# print("------------")
"""
Apelarea functiei cu return se va face specificand numele functiei
        urmat de doua paranteze iar in corpului functiei se va specific un keyword numit "return".
In momentul in care codul va fi executat, sistemul va cauta adresa de memorie care poarta numele
        de salut, va citi codul stocat la acea adresa de memorie si il va executa
Prin intermediul keyword-ului return, noi putem aloca rezultatul functiei unei variabile, sau trimite
        rezultatul catre un sistem extern
Daca o functie nu are return si totusi incercam sa printam rezultatul functiei, sa il alocam unei
        varibile sau sa il trimitem catre un sistem extern, alocarea/printarea/trimiterea va fi facuta
        cu keyword-ul None
"""


def salut_v1():
    mesaj = 'Hai salut'
    return mesaj

x = salut_v1()  # nu va mai printa pe ecran 'Hai salut' pentru ca functia salut_v1 nu mai are o instructiune
#  in interiorul ei
# print(x)  # se va printa de data asta cuvintele Hai salut in loc de cuvantul None, pentru ca am instructiune de return in functie
print("------------")


def salut_v2():
    return 'Hai salut'


#
#
x = salut_v2()
print(x)  # se vor printa tot cuvintele Hai salut
print("------------")
"""
Apelarea functiei cu parametri se va face specificand numele functiei
        urmat de doua paranteze iar intre paranteze se va specifica numele informatiei care se doreste
        a fi parametrizata
Parametrizarea inseamna oferirea posibilitatii de a executa functia de mai multe ori cu valori diferite

Daca nu folosim parametri, si folosim valori efective in corpul functiilor (sau in cod in general)
        atunci vorbim despre o actiune care se numeste "hardcodare" (hardcoding)
"""


# Am definit o functie prin care am parametrizat userul caruia vrem sa ii spunem Salut
# Am vrut sa facem asta pentru ca am vrut sa putem sa salutam mai multe persoane

def salut_user(user):
    print(f'Salut {user}')

"""
user specificat intre paranteze rotunde reprezinta un template, sau o variabila care va stoca
        valoarea efectiva a userului caruia vrem sa ii spunem Salut
user specificat intre acolade reprezinta aceeasi variabila care a venit prin parametru si care va fi
        folosita pentru executarea corpului functiei
"""
salut_user('Mihai')
salut_user("Dan")
print("------------")
"""
Apelarea functiei se va face prin specificarea intre paranteze rotunde a valorii pe care
        vrem sa o trimitem
Daca o functie a fost definita cu parametri, este obligatoriu sa fie si apelata cu argumente
Daca functia a fost definita cu parametri si apelata fara argumente, atunci sistemul va returna eroare
        in consola: TypeError: salut_user() missing 1 required positional argument: '<nume_parametru>'
In momentul apelarii, valoarea sau valorile pe care le scriem intre paranteze se numesc argumente

definire = parametri
apelare = argumente
"""

# Apelarea functiei cu o valoare trimisa prin input

# user = input("Introdu numele utilizatorului pe care vrei sa il saluti: ")
# salut_user(user)
print("------------")


# Apelarea functiei intr-un for, pentru parcurgerea unei liste
lista_nume = ['Bogdan', 'Mircea', 'Luci', 'Raluca', 'Tavi', 'Mihai', 'Andreea']

for nume in lista_nume:
    salut_user(nume)
print("------------")


# Putem sa definim si functii cu mai mult de un parametru
# O functie poate sa aiba oricat de multi parametri avem nevoie
def salut_personal(nume, prenume):
    print(f'Salut {nume} {prenume}')


salut_personal("Ion", "Ion")
print("------------")


# Putem sa definim o functie in care parametrii sa fie optionali (au valoare default definita de noi)
# (adica apelarea functiei se poate face fie cu argumente fie fara)

def salut_user_valori(nume='sorin', prenume='anton'):
    prenume = prenume.upper()
    print(f'Hello {nume} {prenume}')


salut_user_valori("mihai", "alexandru")
salut_user_valori()  # In cazul in care nu specificam parametri, valorile implicite care se vor folosi sunt cele de mai sus
print("------------")


def argumente_multiple(*args):
    print("test")


argumente_multiple("Maria")
argumente_multiple("Anton", "Marian")
argumente_multiple(1, 2, 3, 4, 5, 6)
print("------------")


def calculeaza_suma(*num):
    suma = 0
    for n in num:
        suma = suma + n
    print(f"Suma numerelor care au fost calculate este : {suma}")


calculeaza_suma(1)
calculeaza_suma(12, 34)
calculeaza_suma(125678, 235, 12, 1, 34, 56)
print("------------")

def calculeaza_suma_a_3_nr(a, b, c):
    return a + b + c

suma_a_3_nr = calculeaza_suma_a_3_nr(4, 5, 6)
print(suma_a_3_nr)

# produsul cifrelor unui numar #

def produsul_cifrelor(n):
    produs = 1

    while n != 0:
        produs = produs * (n % 10)
        n = n // 10

    return produs

print(f"Produsul cifrelor numarului este: {produsul_cifrelor(6531)}")

def plus(*args):
    print(sum(args))


plus(1, 4, 5)
print("------------")

# calculati produsul oricarui numar cu 54 #

def produs(a, b=54):
    return a * b


rezultat = produs(6332, 7)
rezultat4 = produs(6332)
rezultat2 = produs(a=6332, b=7)
rezultat3 = produs(b=65, a=5)
print(rezultat)
print(rezultat2)
print(rezultat3)
print(rezultat4)

# calculati restul impartirii unui numar la 7 #

def rest(a, b=7):
    return a % b

print(rest(88))


# scrieti o functie care verifica daca numarul introdus de la tastatura (input) este par. daca este, printati "este par",
# daca nu, nu faceti nimic

def este_par(n):
    if n % 2 == 0:
        print("este par!")
        return True
    else:
        print("nu este par!")
        return False

numar = int(input("n="))
este_par(numar)  # !!! asa apelez o functie !!!


"""Exista situatii in care codul nostru poate sa returneze o eroare, caz in care executia
urmatoarelor linii de cod se va opri. In cazul in care nu ne dorim oprirea codului,
putem sa facem ceea ce se numeste tratarea exceptiilor.

Structura tratarii exceptiilor:

try -> inceputul blocului de exceptie
caracterul “:” marcheaza inceputul blocului de cod care se incearca sa se execute
blocul de cod care se incearca sa se execute
except -> inceputul blocului de tratare a exceptiei
caracterul “:” marcheaza inceputul blocului de cod de tratare a exceptiei
blocul de cod care se executa atunci cand se reproduce exceptia
"""

print(10/0)   # va returna eroare

try:
    print(10 / 0)
except:
    print("impartirea la 0 nu este permisa")

"""Exista situatii in care codul nostru poate sa returneze o eroare,
caz in care executia urmatoarelor linii de cod se va opri.
In cazul in care nu ne dorim oprirea codului, putem sa facem ceea ce se numeste tratarea exceptiilor.

Structura tratarii exceptiilor:

try -> inceputul blocului de exceptie
caracterul “:” marcheaza inceputul blocului de cod care se incearca sa se execute
blocul de cod care se incearca sa se execute
except -> inceputul blocului de tratare a exceptiei
caracterul “:” marcheaza inceputul blocului de cod de tratare a exceptiei
blocul de cod care se executa atunci cand se reproduce exceptia
"""

nota = int(input("Va rugam introduceti nota care trebuie sa fie procesata"))

if nota < 5:
    raise Exception("Nota studentului este prea mica")