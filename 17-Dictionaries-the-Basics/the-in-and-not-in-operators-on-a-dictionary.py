print("era" in "watermelon")
print("z" not in "watermelon")


print(10 in [10, 20, 30])
print(20 not in [10, 15, 30])

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water":["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasour", "Venusaur", ]
}

print("Fire" in pokemon)
print("Grass" in pokemon)
print("Electric" not in pokemon)
print("fire" not in pokemon)

if "Zombie" in pokemon:
    print(pokemon["Zombie"])

else:
    print("The category of zombie doesn't exist!")

