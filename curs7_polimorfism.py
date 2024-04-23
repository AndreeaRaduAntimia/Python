# 1. Polimorfism prin functii cu parametri default
def sir_numere_pare(range_end, range_beginning=0, range_step=1):
    for i in range(range_beginning, range_end + 1, range_step):
        if i % 2 == 0:
            print(f"Numarul {i} este par")
        else:
            print(f"Numarul {i} este impar")


sir_numere_pare(10, 0, 1)
sir_numere_pare(10, 4)
sir_numere_pare(10, range_step=4)


# 2. Polimorfism prin functii cu *args
def calcul_suma_numere(*numbers):
    suma = 0
    for number in numbers:
        suma = suma + number
    return suma


print(calcul_suma_numere(1))
print(calcul_suma_numere(2, 6))
print(calcul_suma_numere(578901256, 789013476, 56))
print(calcul_suma_numere(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27))


def accesare_elemente_dictionar(**kwargs):
    for key, value in kwargs.items():
        print(f"Detalii despre apa: {key}")
        for key_inner, value_inner in value.items():
            if key_inner == "promovare":
                print(f'Apa {key} are {key_inner}: {value_inner["reclama"]}')
            elif key_inner == "televiziune promovare":
                print(f"Televiziunile pe care se promoveaza sunt:", end=" ")
                for televiziuni in value_inner:
                    print(televiziuni, end=" ")
            else:
                print(f"Apa {key} are {key_inner} : {kwargs[key][key_inner]}")

# Exemplu: Functia print este o functie polimorfica pentru ca poate sa fie apelata cu cate argumente avem nevoie
print(len("abc"))
print(len([1, 2, 3, 4]))


# Mai jos am definit o functie cu comportament polimorfic pentru ca am dat lui z valoarea default 0
def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))

# polimorfism prin reimplementarea metodei din clasa parinte in clasa copil

class Animal:
    def sound(self):
        print("miau")


class Catel(Animal):
    def sound(self):
        print("ham")


catel = Catel()
catel.sound()

# Putem sa folosim polimorfismul si in metodele de clasa prin faptul ca implementam doua metode cu acelasi nume in clase diferite
# Ele vor fi diferentiate prin faptul ca vor fi apelate prin obiecte diferite
class Romania:
    def language(self):
        print("Romanian")

class USA:
    def language(self):
        print("English")


obj_ro = Romania()  # Am instantiat un obiect al clasei Romania
obj_usa = USA()  # Am instantiat un obiect al clasei USA
for country in (obj_ro, obj_usa):  # Am iterat prin obiectele create
    country.language()  # am apelat functia language, care pentru fiecare obiect va printa altceva

# Putem sa implementam polimorfismul si in raport cu mostenirea, prin faptul ca reimplementam in clasa copil o metoda care exista in clasa parinte

class Bird:
    def describe(self):
        print("I'm a bird")

    def fly(self):  # Am definit metoda fly in clasa parinte Bird
        print("Flu Flu! I'm flying")


class Parrot(Bird):
    def talk(self):
        print("I also can talk")


class Penguin(Bird):
    def fly(self):  # Am redefinit metoda fly in clasa copil Penguin, cu un comportament specific acestei clase
        print("I actually can't fly. But that's ok, I'm dressed stylish.")


random_bird = Bird()  # am instantiat un obiect al clasei Bird
random_bird.describe()
random_bird.fly()  # am apelat metoda fly din clasa Bird. Va printa pe ecran Flu Flu! I'm flying
print('------------------------')

polly = Parrot()  # am instantiat un obiect al clasei Parrot
polly.describe()
polly.talk()
polly.fly()  # am apelat metoda fly care nu e implementata in clasa Parrot, deci va fi apelata din clasa parinte Bird. Va printa pe ecran Flu Flu! I'm flying
print('------------------------')

pingu = Penguin()  # am instantiat un obiect al clasei Penguin
pingu.describe()
pingu.fly()  # am apelat metoda fly care e implementata in clasa Penguin, deci va fi apelata de aici. Va printa pe ecran I actually can't fly. But that's ok, I'm dressed stylish.
