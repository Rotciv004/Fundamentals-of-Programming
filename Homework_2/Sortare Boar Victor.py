import random
#from random import *

def read_random_list(lenght_of_list: int, NumberList: list):

    """
    :param lenght_of_list:
    :param NumberList:
    :return:
    """

    for indice in range(1, lenght_of_list + 1):
        NumberList.append(random.randint(0, 100))

    print("Acestea sunt numerele random de la 0 la 100 alese pentru lista ta de "+str(lenght_of_list)+" numere: "+str(NumberList))

def Verification_if_a_list_is_ascending_order(lenght_of_list:int ,NumberList:list)-> bool:

    """
    :param lenght_of_list:
    :param NumberList:
    :return:
    """

    for indice in range(1, lenght_of_list+1):
        if NumberList[indice]<NumberList[indice-1]:
            return False

    return True

def BogoSort(lenght_of_list: int, pass_partial_prints: int, NumberList: list):

    contor_afisari_partiale=0

    while not Verification_if_a_list_is_ascending_order(lenght_of_list,NumberList):
        if contor_afisari_partiale == pass_partial_prints:
            print(NumberList)
            contor_afisari_partiale=0
        else:
            contor_afisari_partiale=contor_afisari_partiale+1

        Random.shuffle(NumberList)

def ShellSort(lenght_of_list: int, pass_partial_prints: int, NumberList: list):

    """
    :param lenght_of_list:
    :param pass_partial_prints:
    :param NumberList:
    :return:
    """

    Selection_pass = lenght_of_list // 2
    contor_partial_prints=0

    while Selection_pass > 0:

        for partial_list_index in range(Selection_pass, lenght_of_list):

            value_of_partial_list_index = NumberList[partial_list_index]
            copy_partial_index = partial_list_index

            while copy_partial_index >= Selection_pass and NumberList[copy_partial_index - Selection_pass] > value_of_partial_list_index:
                NumberList[copy_partial_index] = NumberList[copy_partial_index - Selection_pass]
                copy_partial_index = copy_partial_index - Selection_pass

            NumberList[copy_partial_index] = value_of_partial_list_index

            if contor_partial_prints == pass_partial_prints:
                print(NumberList)
                contor_partial_prints = 0
            else:
                contor_partial_prints = contor_partial_prints + 1

        Selection_pass = Selection_pass // 2





while True:
    NumberList= list()
    lenght_of_list = 0
    pass_patial_prints = 0
    verification_for_command_1=False

    print("1. Genereaza o lista")
    print("2. Sorteaza lista prin metoda BogoSort")
    print("3. Sorteaza lista prin metoda ShellSort")
    print("4. Iesire")

    command=int(input("Introdu o comanda --> "))

    if command==1:
        lenght_of_list = int(input("Introdu cate numere vrei sa ai in lista: "))
        pass_patial_prints = int(input("Introdu un pass pentru a vedea din cat in cat sa se afize listele sortate: "))
        read_random_list(lenght_of_list, NumberList)
        verification_for_command_1= True
        command=int(input("Introdu o noua comanda --> "))

    elif command==4:
        print("Ai iesit din program")
        break

    else:
        print("Pentru a genera o sortare, trebuie mai intai sa creezi o lista")

    if command==2 and verification_for_command_1==True:
        BogoSort(lenght_of_list, pass_patial_prints, NumberList)
        print(NumberList)

    elif command==3 and verification_for_command_1==True:
        ShellSort(lenght_of_list, pass_patial_prints, NumberList)
        print(NumberList)

    elif command==4:
        print("Ai iesit din program")
        break