from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue

class Superheroe:
    def __init__(self, heroe):
        self.name = heroe["name"]
        self.real_name = heroe["real_name"]
        self.first_appearance = heroe["first_appearance"]
        self.is_villain = heroe["is_villain"]
        self.short_bio = heroe["short_bio"]

    def __str__(self):
        return f"{self.name}, {self.real_name} - {'Villano' if self.is_villain else 'Héroe'}"

lista_superheroes = List()
for heroe in superheroes:
    nuevo_heroe = Superheroe(heroe)
    lista_superheroes.append(nuevo_heroe)

lista_superheroes.add_criterion("name", lambda h: h.name)
lista_superheroes.add_criterion("real_name", lambda h: h.real_name or "")
lista_superheroes.add_criterion("first_appearance", lambda h: h.first_appearance)

#A Listado ordenado de manera ascendente por nombre de los personajes.
print("\nListado ordenada por nombre: ")
lista_superheroes.sort_by_criterion("name")
lista_superheroes.show()

#B Determinar en que posicion esta The Thing y Rocket Raccoon.
print(f'\nThe Thing está en la posición {lista_superheroes.search("The Thing", "name")}')
print(f'Rocket Raccoon está en la posición {lista_superheroes.search("Rocket Raccoon", "name")}')

#C Listar todos los villanos de la lista.
villanos=List()
for h in lista_superheroes:
    if h.is_villain:
        villanos.append(h)

print("\nLista de villanos: ")
villanos.show()

#D Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
cola_villanos=Queue()
for v in villanos:
    cola_villanos.arrive(v)

print("\nLos villanos que aparecieron antes de 1980 son: ")
while cola_villanos.size() > 0:
    villano= cola_villanos.attention()

    if villano.first_appearance < 1980:
        print(f'{villano.name} en {villano.first_appearance}')

#E Listar los superheores que comienzan con  Bl, G, My, y W.
prefijos= ("Bl", "G", "My", "W")
heroes_prefijos= List()

for s in lista_superheroes:
    if s.name.startswith(prefijos):
        heroes_prefijos.append(s)

print("\nLos heroes que empiezan con Bl, G, My y W son:")
heroes_prefijos.show()

#F Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
print("\nLista ordenada por nombre real: ")
lista_superheroes.sort_by_criterion("real_name")
lista_superheroes.show()

#G Listado de superheroes ordenados por fecha de aparación.
print("\nLista ordenada por fecha de aparición: ")
lista_superheroes.sort_by_criterion("first_appearance")
lista_superheroes.show()

#H Modificar el nombre real de Ant Man a Scott Lang.
pos_antman = lista_superheroes.search("Ant Man", "name")
if pos_antman is not None:
    lista_superheroes[pos_antman].real_name = "Scott Lang"
    print(f"\nSe actualizó el nombre real de Ant Man por {lista_superheroes[pos_antman].real_name}")
else:
    print("\nAnt Man no se encontró en la lista.")

#I Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print("\nPersonajes que en sus biografias incluyen time-traveling o suit: ")
for s in lista_superheroes:
    if "time-traveling" in s.short_bio or "suit" in s.short_bio:
        print(s.name)

#J Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
lista_eliminados=List()
nombres= ["Electro", "Baron Zemo"]

for n in nombres:
    pos = lista_superheroes.search(n, "name")

    if pos is not None:
        lista_eliminados.append(lista_superheroes.pop(pos))

print("\nSe elimino de la lista los siguientes personajes: ")
lista_eliminados.show()