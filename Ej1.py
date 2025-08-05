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

#A Funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
def buscar_heroe(lista, nombre, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == nombre:
        return True
    
    return buscar_heroe(lista, nombre,indice+1)

if buscar_heroe(superheroes,"Capitan America"):
    print("El Capitan America está en la lista")
else:
    print("El Capitan America no está en la lista")

#B funcion recursiva para listar los superheroes de la lista.
def listar_heroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    return listar_heroes(lista, indice+1)

print("\nListado de superheroes:")
listar_heroes(superheroes)
