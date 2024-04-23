# operatii aritmetice

x = 20
y = 101
y = 102
z = 4

print(x + y)
print("---------------")
print(x ** y)
print("---------------")
print(y % x)
print(y / x)
print("---------------")
print(y // x)
print("---------------")

a = 3
b = 4
print("---------------")

# tipuri de atribuire echivalenta
a += 3  # prima suprascriere
a = a + 3  # a doua suprascriere
print(a)

print("---------------")
c = 6
d = 5
print(c == d)
print(c != d)

print(d >= c)
print(c > d)
print("---------------")

c *= 3
c = c * 3
d /= 7
d = d / 7
print(c, d)
print("---------------")
print(c == d)

print("---------------")
a = 4
b = 4

print(a > b or b < 7)
print(a <= b < 5)
print("---------------")

angajat = True
este_par = False

print(not angajat)
print(not (not este_par))
print("---------------")
x = 10 + 25 / 5 - 1
print(int(x))

x = '11'
y = '14.25'
print(type(x))
print(x + y)
print("---------------")

a = 100
b = 9
print(a % b)
print("---------------")

adresa1 = "florilor"
adresa2 = "Strada Florilor nr 5"
adresa3 = "    "
print(adresa2[0:6])
print(adresa2[0:16])
print(adresa2[7:16])
print(adresa2[0:6:2])
print(adresa2[0:10:3])
print("---------------")

# assert

an_nastere = 1964

"""varifica daca valoarea variabilei an_nastere este 1964 - daca este adevarat, trece mai departe, daca nu, returneaza
eroare"""
assert an_nastere == 1964
# assert an_nastere == 1963, f"Valoarea obtinuta nu este cea corecta. Expected:1963, Actual: {an_nastere}"

assert an_nastere != 1963  # verifica daca valoarea an_nastere este diferita de 1963
print("Codul meu")

# assert an_nastere != 1964
print("Codul meu 2")
print("---------------")

# string slicing sau substringuri

s1 = "La Sinaia este zapada"
s2 = s1[3:9]  # stringul este taiat de la indexul 3 pana la indexul 9-1(8) # Sinaia
s3 = s1[3:6]  # Sin

print(s1[::-1])  # inversarea stringului
print(s1[-1])  # printeaza caracterul de pe indexul numarat invers de la 0, in cazul asta ultimul caracter al stringului
print(s1[-6])
print("---------------")

# string methods

numar = "123456123456"
numar2 = "12345F123456"
adresa = "florilor"
adresa2 = "Florilor"

print(numar.replace("1", "A"))  # incoluieste substringul 1 cu noua valoare data de noi litera A de fiecare data cand # il intalneste
print(numar.replace("1", "A", 1))  # incoluieste substringul 1 cu noua valoare data de noi litera A o singura data
print(adresa.upper())
print(adresa.index("l"))
print(adresa.islower())
print(adresa2.islower())
print(numar.islower())
print(numar.isupper())
print(numar2.isupper())
print("---------------")

text = "Mama are nuci"

x = text.split()  # desparte stringul intr-o lista de stringuri cu delimitatorul default spatiul
print(x)
