"""
Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
a)funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
b)funcion recursiva para listar los superheroes de la lista.
"""
superheroes = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Spider-Man",
    "Iron Man",
    "Capitan America",
    "Thor",
    "Hulk",
    "Black Panther",
    "Flash",
    "Green Lantern",
    "Doctor Strange",
    "Wolverine",
    "Aquaman",
    "Scarlet Witch"
]

#A funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
def buscar_heroe(lista, nombre):
    if len(lista) == 0:
        return False
    if lista[0] == nombre:
        return True
    return buscar_heroe(lista[1:], nombre)

nombre = "Capitan America"

if buscar_heroe(superheroes, nombre):
    print(nombre ," está en la lista.")
else:
    print(nombre, " no está en la lista.")

#B funcion recursiva para listar los superheroes de la lista.
def listar_heroes(lista):
    if len(lista) == 0:
        return
    print(lista[0])
    listar_heroes(lista[1:])

print("Listado de super heroes: ")
listar_heroes(superheroes)

