# 3 #
def numar_caractere(nume, prenume, nume_mijlociu):
    caractere_total = 0
    for caracter in nume:
        caractere_total += 1
    for caracter in prenume:
        caractere_total += 1
    for caracter in nume_mijlociu:
        caractere_total += 1
    return caractere_total


caractere_numele_meu = numar_caractere("Razvan", "Daniel", "Corjos")
print(caractere_numele_meu)


# 4 #
def aria_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria


aria_mea = aria_dreptunghi(lungime=int(input("Va rog introduceti lungimea dreptunghiului")),
                           latime=int(input("Va rog introduceti latimea dreptunghiului")))
print(f"Aria dreptunghiului meu este: {aria_mea}")

#
# 5 #
def aria_cercului(raza):
    pi = 3.14
    raza = float(raza)
    area = pi * raza * raza
    return area
    # print("Aria cercului cu raza {0} este {1}".format(raza, area))

aria_mea = aria_cercului(raza=input("Va rugam introduceti raza cercului"))
print(f"Aria cercului meu va fi: {aria_mea}")


# 6 #
def contine_caracter(x, fraza):
    if x in fraza:
        return True
    # else:
    #     return False
    # SAU #
    return False


a = contine_caracter("3", "Mama are 3 mere")
b = contine_caracter("4", "Mama are 3 mere")
print(a)
print(b)


# 7 #
def numara_caractere_lower_si_upper(fraza):
    litere_mari = 0
    litere_mici = 0
    for caracter in fraza:
        if caracter.isupper():
            litere_mari += 1
        elif caracter.islower():
            litere_mici += 1
        else:
            print("Caracterul nu este litera!")
    print(f"Fraza mea are {litere_mici} caractere lower si {litere_mari} caractere upper")


numara_caractere_lower_si_upper("Mama are 3 MERE VERZI si 7 MERE roSIi #%%#$")


# 8 #
def sorteaza_numere_pozitive(lista_totala_numere):
    lista_numere_pozitive = []
    for nr in lista_totala_numere:
        if nr > 0:
            lista_numere_pozitive.append(nr)
        else:
            print("Numarul nu este pozitiv!")
    return lista_numere_pozitive


numere_pozitive = sorteaza_numere_pozitive([1, 3, 4, 6.0, -3, -7.1, -6, 33])
print(numere_pozitive)


# 9 #
def comparator(x, y):
    if x > y:
        print("Primul numar este mai mare decat al doilea")
    elif x < y:
        print("Primul numar este mai mic decat al doilea")
    else:
        print("Numerele sunt egale")


comparator(3, 4)
comparator(4, 3)
comparator(3, 3)
