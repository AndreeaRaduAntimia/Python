# Exercitiu 1: Se citeşte un număr natural. Se cere să se decidă dacă este prim sau nu.
n = int(input("n="))

prim = False

# numerele prime sunt mai mari decat 1
if n > 1:
    # cauta divizori
    for i in range(2, n):
        if (n % i) == 0:
            prim = True
            break

# verifica daca flagul este True
if prim:
    print(n, "nu este prim!")
else:
    print(n, "este prim")


# Exercitiu 2: Vreau sa parcurg o lista de elemente si sa printez fiecare element din lista
lista_studenti_indragostiti_de_while = ["ramona", "catalin", "laurentiu", "george", "ionut", "dorin"]
i = 0
while i < len(lista_studenti_indragostiti_de_while):
    print(f"Studentul curent este: {lista_studenti_indragostiti_de_while[i]}")
    i += 1

# Exercitiu 3: Vreau sa il inlocuiesc pe Dorin cu Andreea pentru ca lui Dorin nu ii place while
i = 0
while i < len(lista_studenti_indragostiti_de_while):
    if lista_studenti_indragostiti_de_while[i] == "dorin":
        lista_studenti_indragostiti_de_while[i] = "andreea"
    i += 1
print(f"Lista finala dupa ce dorin ne-a parasit este: {lista_studenti_indragostiti_de_while}")

# Exercitiu 4: Vreau sa il inlocuiesc pe Laurentiu cu Dorin pentru ca Dorin s-a razgandit si l-a dat pe George afara de entuziasm
while i < len(lista_studenti_indragostiti_de_while):
    if lista_studenti_indragostiti_de_while[i] == "dorin":
        lista_studenti_indragostiti_de_while[i] = "andreea"
        break
    i += 1
print(f"Lista finala dupa ce dorin l-a dat afara pe george este: {lista_studenti_indragostiti_de_while}")

# Exercitiu 4: Realizați un program care afișează suma numerelor impare și suma numerelor pare dintr-o listă."""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
suma_i = 0
suma_p = 0
for x in lista:
    if x % 2 != 0:
        suma_i = suma_i + x
    else:
        suma_p = suma_p + x
print("Suma imparelor =", suma_i)
print("Suma parelor =", suma_p)

# sau

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
suma_i = 0
suma_p = 0
i = 0
lenght = len(lista)
while i < lenght:
    if lista[i] % 2 != 0:
        suma_i = suma_i + lista[i]
    else:
        suma_p = suma_p + lista[i]
    i += 1
print("Suma imparelor =", suma_i)
print("Suma parelor =", suma_p)

# Exercitiu 5: Fiind dat un șir de caractere, afișați toate vocalele pe care le conține."""

sir = 'Îmi place Python!'
vocale = ['a', 'e', 'i', 'o', 'u', 'ă', 'â', 'î', 'A', 'E', 'I', 'O', 'U', 'Ă', 'Â', 'Î']
# pentru fiecare caracter din șir
for c in sir:
    # dacă se găsește în lista vocalelor
    if c in vocale:
        print(c)
