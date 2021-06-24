# #Python Programming - pokemon
# #
# #
# #  Mohana Kamanooru 06/10/2020
# #

# Ask the user for the type of a Pokémon and the first letter of its name
type_pokemon = input("Please enter the type of pokemon (Fire, Water, Grass, Electric:")
first_letter = input("Please enter the first letter from( S T C M B O P V ):")

if(type_pokemon.lower() == "fire"):

    if(first_letter.upper() == "S"):
        print("Name suggestion is : Squirtle")
    elif(first_letter.upper() == "T"):
        print("Name suggestion is : Tentacool")
    else:
        print("No name suggestions are available")
        
elif(type_pokemon.lower() == "water"):

    if(first_letter.upper() == "C"):
        print("Name suggestion is : Charmander")
    elif(first_letter.upper() == "M"):
        print("Name suggestion is : Moltres")
    else:
        print("No name suggestions are available")

elif(type_pokemon.lower() == "grass"):

    if(first_letter.upper() == "B"):
        print("Name suggestion is : Bulbasaur")
    elif(first_letter.upper() == "O"):
        print("Name suggestion is : Oddish")
    else:
        print("No name suggestions are available")

elif(type_pokemon.lower() == "electric"):

    if(first_letter.upper() == "P"):
        print("Name suggestion is : Pikachu")
    elif(first_letter.upper() == "V"):
        print("Name suggestion is : Voltorb")
    else:
        print("No name suggestions are available")

else :
    print("No Pokemon type is defined")
    
