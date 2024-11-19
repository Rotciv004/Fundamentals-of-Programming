import random
#from random import *
from timeit import timeit

def read_random_list(lenght_of_list: int, NumberList: list):

    """
    :param lenght_of_list:
    :param NumberList:
    :return:
    """

    for indice in range(1, lenght_of_list + 1):
        NumberList.append(randint(0, 100))

    print("Acestea sunt numerele random de la 0 la 100 alese pentru lista ta de "+str(lenght_of_list)+" numere: "+str(NumberList))

def Verification_if_a_list_is_ascending_order(lenght_of_list:int ,NumberList:list)-> bool:

    """
    :param lenght_of_list:
    :param NumberList:
    :return:
    """

    for indice in range(0, lenght_of_list):
        if NumberList[indice]<NumberList[indice-1]:
            return False

    return True

def BogoSort(lenght_of_list: int, pass_partial_prints: int, NumberList: list):
    """
    :param lenght_of_list:
    :param pass_partial_prints:
    :param NumberList:
    :return:
    """

    contor_afisari_partiale=0

    while not Verification_if_a_list_is_ascending_order(lenght_of_list,NumberList):
        if contor_afisari_partiale == pass_partial_prints:
            print(NumberList)
            contor_afisari_partiale=0
        else:
            contor_afisari_partiale=contor_afisari_partiale+1

        random.shuffle(NumberList)


def BogoSort_(lenght_of_list: int, NumberList: list):
    """
    :param lenght_of_list:
    :param NumberList:
    :return:
    """

    while not Verification_if_a_list_is_ascending_order(lenght_of_list,NumberList):
        random.shuffle(NumberList)



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





def ShellSort_(lenght_of_list: int, NumberList: list):
    """
    :param lenght_of_list:
    :param NumberList:
    :return:
    """

    Selection_pass = lenght_of_list // 2

    while Selection_pass > 0:

        for partial_list_index in range(Selection_pass, lenght_of_list):

            value_of_partial_list_index = NumberList[partial_list_index]
            copy_partial_index = partial_list_index

            while copy_partial_index >= Selection_pass and NumberList[copy_partial_index - Selection_pass] > value_of_partial_list_index:
                NumberList[copy_partial_index] = NumberList[copy_partial_index - Selection_pass]
                copy_partial_index = copy_partial_index - Selection_pass

            NumberList[copy_partial_index] = value_of_partial_list_index

        Selection_pass = Selection_pass // 2





def TimeT_function_ShellSort_Best_case(NumberList_lenght :int):
    for index in range(1, NumberList_lenght + 1):
        NumberList.append(index)

    print(NumberList)
    print(timeit(lambda: ShellSort_(NumberList_lenght, NumberList), number=1))


def TimeT_function_BogoSort_Best_case(NumberList_lenght :int):
    for index in range(1, NumberList_lenght + 1):
        NumberList.append(index)

    print(NumberList)
    print(timeit(lambda: BogoSort_(NumberList_lenght, NumberList), number=1))


def TimeT_function_ShellSort_Worst_case(NumberList_lenght :int):
    for index in range(NumberList_lenght, 0,-1):
        NumberList.append(index)

    print(NumberList)
    print(timeit(lambda: ShellSort_(NumberList_lenght, NumberList), number=1))


def TimeT_function_BogoSort_Worst_case(NumberList_lenght :int):

    for index in range(NumberList_lenght, 0, -1):
        NumberList.append(index)

    print(NumberList)
    print(timeit(lambda: BogoSort_(NumberList_lenght, NumberList), number=1))




while True:
    NumberList = []
    number_list_lenght = 0
    pass_partial_prints = 0
    verification_if_we_input_firstly_a_NumberList=False

    print("1. Generate a random list")
    print("2. Sort the list using BogoSort")
    print("3. Sort the list using ShellSort")
    print("4. The best case for Shell sort")
    print("5. The best case for Bogo sort")
    print("6. The medium case for Shell sort")
    print("7. The medium case for Bogo sort")
    print("8. The worst case for Shell sort")
    print("9. The worst case for Bogo sort")
    print("10. Exit")

    command=int(input("Input a command --> "))

    if command==1:
        number_list_lenght = int(input("Input the lenght of your list: "))
        pass_partial_prints = int(input("Input a pass value to see the partial results: "))
        read_random_list(number_list_lenght, NumberList)
        verification_if_we_input_firstly_a_NumberList= True
        command=int(input("Input a new command --> "))

    elif command == 4:
        print("Cel mai buna complexitate in cazul ShellSort este atunci cand toate / aproape numerele sunt in ordinea pe care vrem sa o cautam ,iar programul va avea o complexitate O(n*log n). Acest lucru va avea loc in cazul in care H[s+1]%H[s]==0")

        TimeT_function_ShellSort_Best_case(5)
        TimeT_function_ShellSort_Best_case(10)
        TimeT_function_ShellSort_Best_case(20)
        TimeT_function_ShellSort_Best_case(40)
        TimeT_function_ShellSort_Best_case(80)

    elif command == 5:

        print("Cel mai bun caz metoda BogoSort va avea o complexitate de O(n), elementele fiind deja sortate in ordinea dorita")

        TimeT_function_BogoSort_Best_case(5)
        TimeT_function_BogoSort_Best_case(10)
        TimeT_function_BogoSort_Best_case(20)
        TimeT_function_BogoSort_Best_case(40)
        TimeT_function_BogoSort_Best_case(80)

    elif command == 6:
        print("In cazul mediu  favorabil al metodei ShellSort avem o complexitate cuprinsa intre O(n*log n) si O(n^2) si depinde foarte mult de ordinea in care sunt arajate elementele in sir")

    elif command == 7:
        print("In cazul mediu favorabil al metodei BogoSort avem o complexitate de O(n*n!), depinzand foarte mul de faptul ca numerele sunt reordonate aleator")

    elif command == 8:
        print("In cazul cel mai nefavorabil al metodei ShellSort va avea o complexitate de O(n^2) si va avea loc atunci cand H[s]=2^s-1 unde 1<=s<t, t=[log^2 n]-1")

        TimeT_function_ShellSort_Worst_case(5)
        TimeT_function_ShellSort_Worst_case(10)
        TimeT_function_ShellSort_Worst_case(20)
        TimeT_function_ShellSort_Worst_case(40)
        TimeT_function_ShellSort_Worst_case(80)

    elif command == 9:

        print("In cazul secventei BogoSort este de O(n*n!)")

        TimeT_function_BogoSort_Worst_case(5)
        TimeT_function_BogoSort_Worst_case(10)
        TimeT_function_BogoSort_Worst_case(20)
        TimeT_function_BogoSort_Worst_case(40)
        TimeT_function_BogoSort_Worst_case(80)

    elif command == 10:
        print("You exit form the program")
        break

    else:
        print("Firstly you need to create a list")
        command = int(input("Enter a new command --> "))

    if command==2 and verification_if_we_input_firstly_a_NumberList==True:
        BogoSort(number_list_lenght, pass_partial_prints, NumberList)
        print(NumberList)

    elif command==3 and verification_if_we_input_firstly_a_NumberList==True:
        ShellSort(number_list_lenght, pass_partial_prints, NumberList)
        print(NumberList)

