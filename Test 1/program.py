code_list=["Z01","Z02","Z03","Z04","Z05","Z06"] #string
name_list=["Alex","Marius","Vasile","Cristi","Ion","Alin"] #string
type_list=["Carnivores","Carnivores","Herbivores","Herbivores","Omnivores","Carnivores"] #string
species_list=["Dog","Cat","Caw","Shep","Pig","Dog"] #string

def print_animal_list():
    for index in range(0,len(code_list)):
        print(f"{code_list[index]}   {name_list[index]}   {type_list[index]}   {species_list[index]}")

def verify_if_code_already_exist(code:str) -> bool:
    for index in range(0,len(code_list)):
        if code_list[index] == code:
            return True

    return False

def add_an_animal_based_on_secifications(code:str,name:str,type:str,species:str): #1
     if verify_if_code_already_exist(code) == False and len(name) != 0 and len(type) != 0 and len(species) != 0:
         code_list.append(code)
         name_list.append(name)
         type_list.append(type)
         species_list.append(species)

         print("You succesfuly add the animal!")

     else:
         print("ERROR: Your code already exist or a filde is empty! The animal wasn't add!")


def change_the_type_of_animal_based_on_species(type:str, species:str): #2
    if len(type) != 0:
        for index in range(0, len(type_list)):
            if species == species_list[index]:
                type_list[index] = type
        print(f"You modify the type {type} at all your species {species}!")

    else:
        print("ERROR: Type is void! The modification wasn't made!")

def sort_animals_after_species(): #3
    for index in range(0,len(code_list)-1):
        for jndex in range(index+1, len(code_list)):
            if species_list[index] > species_list[jndex]:
                code_list[index], code_list[jndex] = code_list[jndex], code_list[index]
                name_list[index], name_list[jndex] = name_list[jndex], name_list[index]
                type_list[index], type_list[jndex] = type_list[jndex], type_list[index]
                species_list[index], species_list[jndex] = species_list[jndex], species_list[index]

    for index in range(0, len(code_list) - 1):
        for jndex in range(index + 1, len(code_list)):
            if species_list[index] == species_list[jndex] and name_list[index] > name_list[jndex]:
                code_list[index], code_list[jndex] = code_list[jndex], code_list[index]
                name_list[index], name_list[jndex] = name_list[jndex], name_list[index]
                type_list[index], type_list[jndex] = type_list[jndex], type_list[index]
                species_list[index], species_list[jndex] = species_list[jndex], species_list[index]






ADD_AN_ANIMAL = 1
CLASIFICATION_ERROR_CHANGE_AFTER_TYPE = 2
ANIMALS_SORTED_BY_SPECIES = 3
EXIT = 4

while True:
    print("1. Add an animal")
    print("2. Change the type of a species")
    print("3. Animals sorted by species")
    print("4. EXIT")

    command = int(input("Input a command --> "))

    if command == ADD_AN_ANIMAL:
        code = str(input("Input a code for a new animal --> "))
        name = str(input("Input a name for a new animal --> "))
        type = str(input("Input a type for a new animal --> "))
        species = str(input("Input a species for a new animal --> "))

        add_an_animal_based_on_secifications(code,name,type,species)
        print_animal_list()

    elif command == CLASIFICATION_ERROR_CHANGE_AFTER_TYPE:
        species = str(input("Input a species --> "))
        type = str(input("Input a type --> "))

        change_the_type_of_animal_based_on_species(type,species)
        print_animal_list()

    elif command == ANIMALS_SORTED_BY_SPECIES:
        sort_animals_after_species()
        print_animal_list()

    elif command == EXIT:
        print("You close the program!")
        break

    else:
        print("Input command isn't correct! Please retry!")
