"""Având în vedere o matrice de numere întregi A, maximizați valoarea expresiei A[m] - A[n] + A[p] - A[q], unde m, n, p, q sunt indicii de matrice cu
m > n > p > q. Pentru A = [30, 5, 15, 18, 30, 40], valoarea maximă este 32, obținută ca 40 - 18 + 15 - 5. Afișați atât valoarea maximă, cât și expresia
folosită pentru a o calcula."""

def Maximum_value_for_expresion_Am_minus_An_plus_Ap_minus_Aq_in_A_matrix_using_dinamic_implementation(NumberList: list):

    # we initialized intermediar_maximum_values_for_NumberList with values less than (-inf)
    intermediar_maximum_values_for_NumberList = [[[[float('-inf') for _ in range(len(NumberList))] for _ in range(len(NumberList))] for _ in range(len(NumberList))] for _ in range(len(NumberList))]

    # We find the max value in intermediar_maximum_values_for_NumberList
    max_value = -1

    # Go through the intermediar_maximum_values_for_NumberList to find the intermediar_maximum_values_for_NumberList values
    for first_index in range(len(NumberList)):
        for second_index in range(first_index):
            for third_index in range(second_index):
                for forth_index in range(third_index):
                    # Calculăm valoarea expresiei pentru indicii first_index, second_index, third_index, forth_index
                    intermediar_maximum_values_for_NumberList[first_index][second_index][third_index][forth_index] = max(intermediar_maximum_values_for_NumberList[first_index][second_index][third_index][forth_index] , NumberList[first_index] - NumberList[second_index] + NumberList[third_index] - NumberList[forth_index])
                    print(f"A[{first_index}][{second_index}][{third_index}][{forth_index}] = {intermediar_maximum_values_for_NumberList[first_index][second_index][third_index][forth_index]}")
                    max_value = max(max_value, intermediar_maximum_values_for_NumberList[first_index][second_index][third_index][forth_index])

    # We print intermediar_maximum_values_for_NumberList

    print("Dinamic implementation => "+ str(max_value))


def Maximum_value_for_expresion_Am_minus_An_plus_Ap_minus_Aq_in_A_matrix_using_naiv_implementation(NumberList: list):

    max_sum=0
    max_first_index=-1
    max_second_index=-1
    max_third_index=-1
    max_forth_index=-1

    for first_index in range(3, len(NumberList)):
        for second_index in range(2, first_index):
            for third_index in range(1, second_index):
                for forth_index in range(0,third_index):

                    sum=NumberList[first_index] - NumberList[second_index] + NumberList[third_index] - NumberList[forth_index]

                    if sum>max_sum:

                        max_sum=sum
                        max_first_index=first_index
                        max_second_index=second_index
                        max_third_index=third_index
                        max_forth_index=forth_index


    print("Naiv implementation => A[" + str(max_first_index)+ "] - A[" + str(max_second_index) + "] + A[" + str(max_third_index) + "] - A[" + str(max_forth_index) + "] = " + str(max_sum))



while True:

    NumberList = []

    NumberList_lenght = int(input("Input the lenght of your list. The minimum lenght must be 4"))

    if NumberList_lenght >= 4:

        print("Input the values of your list")

        for index in range(0, NumberList_lenght):
            NumberList.append(int(input("A[" + str(index) + "]= ")))

        print("1. Naiv implementation")
        print("2. Dinamic implementation")

        command=int(input("Input a command -> "))

        if command == 1:
            Maximum_value_for_expresion_Am_minus_An_plus_Ap_minus_Aq_in_A_matrix_using_naiv_implementation(NumberList)

        elif command == 2:
            Maximum_value_for_expresion_Am_minus_An_plus_Ap_minus_Aq_in_A_matrix_using_dinamic_implementation(NumberList)

    else:

        print("The minimum lenght must be 4")