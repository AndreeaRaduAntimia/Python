# liste sau vectori

masini = ["Audi", "BMW", "Ferrari", "Ford", "Opel"]
print(masini)
print(type(masini))
print(masini[0])  # printeaza primul element al listei
print(masini[3])
# print(masini[4])  # returneaza eroare

print(len(masini))
print(masini[len(masini) - 1])  # printeaza ultimul element al listei
print(masini[-1])

print(masini[0:2])  # printeaza primele 2 elemente ale listei
print(masini[0:3:2])  # printam primul si al 3lea element cu pas de 2
print(masini[0], masini[2])

print(masini[2:])
print(masini[::-1])

print("---------------")
lista1 = ["a", "b"]
lista2 = ["c", "d"]
lista3 = lista1 + lista2
print(lista3)
print(lista3 * 3)

# verificati daca substringul "a" se afla in lista 1 sau lista 2 sau lista 3
print("a" in lista1 or "a" in lista2 or "a" in lista3)
print("a" in lista1 or "a" in lista2 and "a" in lista3)

lista1[1] = "f"  # suprascrierea unui element din lista
print(lista1)
lista3.remove("a")  # sterge primul element ce contine stringul a
print(lista3)

del lista3[0]  # sterge primul element din lista

lista2.append("z")  # adaugare la finalul listei de elementul z
print(lista2)
lista2.insert(1, 1)
print(lista2)
print("---------------")

# tupluri
pers1 = ("Mihai", "Popescu", 26, 1.87, "Galati")
pers2 = ("Dana", "Ionescu", 25, 1.67, "Tecuci")

print(pers1)
print(type(pers2))
print(pers2[2:4])
print(pers2[-1])
print(pers2[::-1])
print(len(pers1))
print("Dan" in pers2)
print("Dan" in pers2[0])
print("Petrica" not in pers2)

tuplu1 = (1, 2, 3, 4, 5, 2, 3)
print("3 apare de", tuplu1.count(3), "ori.")
print("---------------")

# seturi
set1 = {1, 2, 3, 4, 7}
print(set1)
print("---------------")
print(len(set1))
set1.pop()
print(set1)
set1.discard(3)
print(set1)
print("---------------")

# dictionare

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "an": 1964
}

print(dict1["an"])
print(len(dict1))

# 2 exemple de cum putem modifica dictionarul
dict1.update({"brand": "Ferrari"})
print(dict1)
dict1["brand"] = "Range Rover"
print(dict1)
dict1["caroserie"] = "break"  # adaugare intrare noua
print(dict1)

del dict1["caroserie"]  # stergere intrare dict
print(dict1)
dict1.pop("an")
print(dict1)
