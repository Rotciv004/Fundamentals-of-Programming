"""Două numere naturale m și n sunt date. Afișați în toate modalitățile posibile numerele de la 1 până la n,
astfel încât între oricare două numere pe poziții consecutive, diferența de valoare absolută să fie de cel puțin m.
Dacă nu există o soluție, afișați un mesaj."""

def Verification_if_we_have_absolute_value_betwen_consecutive_values_in_NumberList(NumberList_lenght: int, NumberList: list, Absolute_value_betwen_consecutive_values_in_NumberList: int) -> bool:

    for index in range(0,NumberList_lenght-1):

        if abs(NumberList[index]-NumberList[index+1]) < Absolute_value_betwen_consecutive_values_in_NumberList:

            return False


    return True



def Verification_if_a_value_is_already_use_in_NumberList(NumberList_lenght: int,wanted_number: int, NumberList: list) -> bool:
    for index in range(0, NumberList_lenght):

        if NumberList[index] == wanted_number:

            return True


    return False


def IterativeBackTracking_for_permutations_where_sub_betwen_consecutive_values_are_equal_or_greater_than_a_value(NumberList_lenght :int, NumberList :list, Absolute_value_betwen_consecutive_values_in_NumberList: int, verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList :bool):

    while len(NumberList)>0:

        find=False

        NumberList[len(NumberList)-1] +=1

        if NumberList[len(NumberList)-1] <= NumberList_lenght and not Verification_if_a_value_is_already_use_in_NumberList(len(NumberList)-1,NumberList[len(NumberList)-1],NumberList):
            find=True

        while not find and NumberList[len(NumberList)-1]<=NumberList_lenght:

            NumberList[len(NumberList) - 1] += 1

            if NumberList[len(NumberList) - 1] <= NumberList_lenght and not Verification_if_a_value_is_already_use_in_NumberList(len(NumberList) - 1, NumberList[len(NumberList) - 1], NumberList):
                find = True


        if not find:

            NumberList.pop()

        elif len(NumberList)< NumberList_lenght:

            NumberList.append(0)

        elif Verification_if_we_have_absolute_value_betwen_consecutive_values_in_NumberList(len(NumberList),NumberList,Absolute_value_betwen_consecutive_values_in_NumberList):
            print(NumberList)
            verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList=True



def RecursiveBackTracking_where_subtraction_betwen_consecutive_values_are_equal_or_greater_than_a_value(NumberList_lenght: int, NumberList: list, Absolute_value_betwen_consecutive_values_in_NumberList: int, verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList: bool):

    for number in range(1, NumberList_lenght+1):

        if not Verification_if_a_value_is_already_use_in_NumberList(len(NumberList),number,NumberList):

            NumberList.append(number)

            if Verification_if_we_have_absolute_value_betwen_consecutive_values_in_NumberList(len(NumberList),NumberList,Absolute_value_betwen_consecutive_values_in_NumberList):

                if len(NumberList) == NumberList_lenght:

                        print(NumberList)
                        verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList = True


            RecursiveBackTracking_where_subtraction_betwen_consecutive_values_are_equal_or_greater_than_a_value(NumberList_lenght, NumberList, Absolute_value_betwen_consecutive_values_in_NumberList, verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList)
            NumberList.pop()




while True:

    print("1. Do the problem in recursive mode")
    print("2. Do the problem in iterative mode")
    print("3. EXIT")

    command=int(input("Input command -> "))

    if command == 1:

        NumberList = []
        NumberList_lenght = int(input("Input the lenght of the list -> "))
        Absolute_value_betwen_consecutive_values_in_NumberList = int(input("Input the absolute value betwen consecutive values in number list -> "))
        verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList = False

        RecursiveBackTracking_where_subtraction_betwen_consecutive_values_are_equal_or_greater_than_a_value(NumberList_lenght, NumberList, Absolute_value_betwen_consecutive_values_in_NumberList, verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList)

        if not verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList:
            print("\nWe do not have any posible ways to order the number to obtain the diference betwen each consecutive term to be at least " + str(Absolute_value_betwen_consecutive_values_in_NumberList))


    elif command == 2:

        NumberList = [0]
        NumberList_lenght = int(input("Input the lenght of the list -> "))
        Absolute_value_betwen_consecutive_values_in_NumberList = int(input("Input the absolute value betwen consecutive values in number list -> "))
        verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList = False

        IterativeBackTracking_for_permutations_where_sub_betwen_consecutive_values_are_equal_or_greater_than_a_value(NumberList_lenght, NumberList, Absolute_value_betwen_consecutive_values_in_NumberList, verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList)

        if not verification_if_we_found_an_absolute_value_betwen_each_sub_betwen_each_consecutive_value_in_NumberList:
            print("\nWe do not have any posible ways to order the number to obtain the diference betwen each consecutive term to be at least " + str(Absolute_value_betwen_consecutive_values_in_NumberList))

    elif command == 3:

        print("you close the program")
        break

    else:

        print("We do not have this command")