pokedex = {}


with open("pokemonlista.txt", "r") as f1:
    for rad in f1:
        rad = rad.strip("\n")
        rad = rad.split()
        pokedex [rad[1]] = (f"index: {rad[0]} typ: {rad[2]}")
            

print(pokedex["Mewtwo"])