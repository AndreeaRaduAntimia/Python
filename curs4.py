"""
3. Structura alternativa IF
If-ul este o structura alternativa prin intermediul careia putem sa executam
un set de instructiuni sau un altul in functie de rezultatul evaluarii unei conditii

Componentele unui if(decizie) sunt:
- inceputul deciziei (IF)
- ramura din dreapta a deciziei (THEN) -> in python este reprezentat de primul set de instructiuni dupa ":"
- ramura din stanga a deciziei (ELSE) - executata cand conditia este evaluata ca FALSE
    -> in python reprezinta al doilea set de instructiuni, plasate dupa semnul ":" de la else
- elif -> o situatie alternativa definita de un alt set de conditii atunci cand avem mai multe situatii posibile

In orice structura alternativa sau repetitiva, blocul de cod care trebuie executat se marcheaza cu indentare
indentare = spatiul lasat intre marginea fisierului si linia de cod

- Ordinea keyword-urilor o sa fie: IF, ELIF, ELSE
"""
# n = 5
#
# if n > 0:
#     print("Numarul este mai mare decat 0!")
# else:
#     print("Numarul nu este mai mare decat 0!")
#
# print("--------------")

"""Se citeste o valoare intreaga. In cazul in care aceasta este para(se imparte exact la 2), se va tipari mesajul 'numar par'.
Altfel, pogramul nu va tipari niciun mesaj"""

# n = int(input("n="))
#
# if n % 2 == 0:
#     print("numar par")
# else:
#     print("numar impar")
#
# print("--------------")

"""Se citesc 3 numere intregi cu zecimala. Cate dintre ele sunt pare?"""

# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# a = 6
# b = 7
# c = 8
#
# d = 0
#
# if a % 2 == 0:
#     d += 1  # d = d+1
# if b % 2 == 0:
#     d += 1
# if c % 2 == 0:
#     d += 1
#
# print(f"Avem {d} numere pare")
# print("--------------")


"""Cum se pun notele la examene"""

# nota = int(input("Introduceti punctajul la examen: "))
#
# if nota > 95:
#     print("Nota obtinuta este 10!")
# elif nota > 85:
#     print("Nota obtinuta este 9!")
# elif nota > 75:
#     print("Nota obtinuta este 8!")
# elif nota > 65:
#     print("Nota obtinuta este 7!")
# elif nota > 55:
#     print("Nota obtinuta este 6!")
# elif nota > 50:
#     print("Nota obtinuta este 5!")
# else:
#     print("Ai picat examenul!")
#
# print("--------------")

##################################################################################
"""
Structuri repetitive = modalitati prin care putem sa executam o serie de statementuri (instructiuni)
de mai multe ori pana cand o anumita conditie nu mai este indeplinita

while = structura repetitiva care este folosita atunci cand vrem sa executam un set de instructiuni pe baza de conditie explicita
for = structura repetitiva care este folosita atunci cand vrem sa executam un set de instructiuni pe baza de range
for each = structura repetitiva care este folosita atunci cand vrem sa iteram prin elementele unei structuri de date

"""
##################################################################################
""""
while = structura repetitiva care instruieste sistemul sa execute un set de instructiuni]
				atata timp cat o conditie este adevarata
Componentele unui while sunt:
1. instructiune de initializare a contorului (optional - doar daca se foloseste contor)
2. inceputul iteratiei (while)
3. conditia de iteratie urmata de :
4. blocul de cod care sa se execute
5. instructiunea de incrementare a contorului / modificare a conditiei pentru a controla iteratia
"""

# count = 1
# while count <= 101:
#     print(f"Dalmatianul curent este: {count}")
#     count += 1  # count = count + 1


"Suma tuturor numerelor de la 1 la 10"
# numar = 1
# suma = 0
# while numar <= 10:
#     suma = suma + numar
#     numar = numar + 1
# else:
#     print(f"Suma calculata este: {suma}")


##################################################################################
"""
for = structura repetitiva care instruieste sistemul sa execute
						un set de instructiuni atata timp cat un contor se afla intr-un range
componentele unui for:
1. contor de iteratie
2. range (start - optional <default 0>, end - obligatoriu, pas de incrementare- optional <> default 1)
3. set de instructiuni de executat
"""
# numar = 10
# suma = 0
# for i in range(1, numar + 1):
#     suma = suma + i
# print("Suma este:", suma)

# exemplu instructiune for intr-o lista
# lista1 = [1, 3, 4, 5]
#
# for el in lista1:
#     print(el)
#
# # exemplu instructiune for intr-un string
# fraza = "Imi place Python"
# print(fraza[0:16])
#
# for c in fraza:
#     print(c)

# for n in range(5):  # de la 0 la 4
#     print(n)
#
# for n in range(1, 6):  # de la 1 la 5
#     print(n)

# for n in range(1, 11, 2):
#     print(n)

# calculez media aritmetica

lista_note = [10, 10, 10, 9, 5, 8, 9]
suma = 0

for i in range(len(lista_note)):
    suma = suma + lista_note[i]

medie = suma / len(lista_note)
print(medie)

"""
functionare:
i = 0 => 0 <7? DA => Suma = 0 + 10 = 10
i = 1 => 1 < 7? DA => Suma = 10 + 10 = 20
i = 2 => 2 < 7? DA => Suma = 20 + 10 = 30
i = 3 => 3 < 7? DA => Suma = 30 + 9 = 39
i = 4 => 4 < 7? DA => Suma = 39 + 5 = 44
i = 5 => 5 < 7? DA => Suma = 44 + 8 = 52
i = 6 => 6 < 7? DA => Suma = 52 + 9 = 61
i = 7 => 7 < 7? NU
medie = 61 / 7  = 8.714285714285714
"""

# rezolvare cu FOR EACH #

# lista_note = [10, 10, 10, 9, 5, 8, 9]
# suma = 0
#
# for nota in lista_note:
#     suma = suma + nota
#
# medie = suma / len(lista_note)
# print(medie)

"""
nota = 10  => suma = 0 + 10 = 10
nota = 10  => suma = 10 + 10 = 20
nota = 10  => suma = 20 + 10 = 30
nota = 9   => suma = 30 + 9 = 39
nota = 5   => suma = 39 + 5 = 44
nota = 8   => suma = 44 + 8 = 52
nota = 9   => suma = 52 + 9 = 61
"""
##################################################################################
"""
for each este o modalitate prin care putem sa iteram printr-o structura de date prin parcurgerea elementelor

Componentele unui foreach
1. Variabila / variabilelel de iteratie
2. structura pe care o parcurgem
3. instructiunile pe care sa le executam
"""
##################################################################################

# break/continue

lista_masini = ["Audi", "BMW", "Mertzan", "Dacia", "Peugeot"]

for masina in lista_masini:
    if masina == "BMW" or masina == "Dacia":
        # break
        print(masina)
    print(f"Va recomand masina {masina}")

