prenume = ['Mihai', 'George', 'Ana', 'Dan', 'Ion', 'Geta', 'Vio']
varsta = [14, 23, 15, 14, 12, 41, 39]

'''
a) Adăugați în liste la final, corespunzător, datele: Andreea, 34 și Ioan, 23. Tipăriți ambele liste apoi.

b) Afișați primele trei elemente din lista prenume.

c) Afișați lista prenume de la dreapta la stânga.

d) Tipăriți elementele cu indicii 2 și 4, apoi de la 0 la 5 din ambele liste.
'''
# a
prenume.append("Andreea")
print(prenume)
varsta.append(34)
print(varsta)

# sau
prenume.insert(len(prenume), "Ioan")
print(prenume)
varsta.insert(len(varsta), 23)
print(varsta)
# b
print(prenume[0:3])

# c
print(prenume[::-1])

# d
print(varsta[2], varsta[4])
print(prenume[0:6])













# # b
# print(prenume[0:3])
#
# # c
# print(prenume[::-1])
#
# # d
# print(prenume[2], prenume[4])
# print(varsta[2], varsta[4])
#
# print(prenume[0:6])
# print(varsta[0:6])

