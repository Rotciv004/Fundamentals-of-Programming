import math

def input_number(complex_numberlist: dict):
    complex_number = input("Input a complex number -> ")
    delete_i = complex_number.split("i")
    real = 0
    imaginary = 0

    if "+" in delete_i[0]:
        numbers = delete_i[0].split("+")
        if len(numbers) == 2:
            real = int(numbers[0])
            imaginary = int(numbers[1])
        else:
            print("ERROR: Invalid input!")
    elif "-" in delete_i[0]:
        numbers = delete_i[0].split("-")
        if len(numbers) == 3 and numbers[0] == "":
            real = -int(numbers[1])
            imaginary = -int(numbers[2])
        elif len(numbers) == 2:
            real = int(numbers[0])
            imaginary = -int(numbers[1])
    else:
        print("ERROR: Invalid input!")

    key = len(complex_numberlist)
    complex_numberlist[key] = [real, imaginary]

def print_numberlists(complex_numberlist: dict):
    for index in range(len(complex_numberlist)):
        if complex_numberlist[index][1] != 0 and complex_numberlist[index][0] != 0:
            if complex_numberlist[index][1] > 0:
                print("C[" + str(index) + "]= " + str(complex_numberlist[index][0]) + "+" + str(complex_numberlist[index][1]) + "i")
            else:
                print("C[" + str(index) + "]= " + str(complex_numberlist[index][0]) + str(complex_numberlist[index][1]) + "i")
        elif complex_numberlist[index][1] == 0 and complex_numberlist[index][0] != 0:
            print("C[" + str(index) + "]= " + str(complex_numberlist[index][0]))
        elif complex_numberlist[index][0] == 0 and complex_numberlist[index][1] != 0:
            print("C[" + str(index) + "]= " + str(complex_numberlist[index][1]) + "i")
        else:
            print("C[" + str(index) + "]= 0")

def remove_elements_from_max_numberlists(complex_numberlist: dict):
    while len(complex_numberlist) > 0:
        complex_numberlist.popitem()

def add_elements_to_max_numberlists(left: int, right: int, complex_numberlist: dict, max_complex_numberlist: dict):
    for index in range(left, right):
        key = len(max_complex_numberlist)
        max_complex_numberlist[key] = [complex_numberlist[index][0], complex_numberlist[index][1]]

def modul_of_complex_numbers(real: int, imaginar: int) -> float:
    return math.sqrt(real**2 + imaginar**2)

def the_length_and_elements_of_a_longest_increasing_subsequence_when_considering_each_number_s_modulus(complex_numberlist: dict):
    max_complex_numberlist = {}
    index_left = 0

    for index_right in range(1, len(complex_numberlist)):
        if modul_of_complex_numbers(complex_numberlist[index_right][0], complex_numberlist[index_right][1]) <= modul_of_complex_numbers(complex_numberlist[index_right - 1][0], complex_numberlist[index_right - 1][1]):
            if len(max_complex_numberlist) < index_right - index_left + 1:
                remove_elements_from_max_numberlists(max_complex_numberlist)
                add_elements_to_max_numberlists(index_left, index_right, complex_numberlist, max_complex_numberlist)

            index_left = index_right

    if len(max_complex_numberlist) < len(complex_numberlist) - index_left:
        remove_elements_from_max_numberlists(max_complex_numberlist)
        add_elements_to_max_numberlists(index_left, len(complex_numberlist) - 1, complex_numberlist, max_complex_numberlist)

    print_numberlists(max_complex_numberlist)
    print(len(max_complex_numberlist))

def verify_if_a_number_is_alredy_in_the_max_numberlist(real: int, imaginar: int, left: int, right: int, complex_numberlist: dict) -> bool:
    for index in range(left, right):
        if real == complex_numberlist[index][0] and imaginar == complex_numberlist[index][1]:
            return True
    return False

def length_and_elements_of_a_longest_subarray_of_distinct_numbers(complex_numberlist: dict):
    max_complex_numberlist = {}
    index_left = 0

    for index_right in range(1, len(complex_numberlist)):
        if verify_if_a_number_is_alredy_in_the_max_numberlist(complex_numberlist[index_right][0], complex_numberlist[index_right][1], index_left, index_right, complex_numberlist):
            if len(max_complex_numberlist) < index_right - index_left + 1:
                remove_elements_from_max_numberlists(max_complex_numberlist)
                add_elements_to_max_numberlists(index_left, index_right, complex_numberlist, max_complex_numberlist)

            index_left = index_right

    if len(max_complex_numberlist) < len(complex_numberlist) - index_left:
        remove_elements_from_max_numberlists(max_complex_numberlist)
        add_elements_to_max_numberlists(index_left, len(complex_numberlist) - 1, complex_numberlist, max_complex_numberlist)

    print_numberlists(max_complex_numberlist)
    print(len(max_complex_numberlist))

complex_numberlist = {0: [1, 12], 1: [3, 10], 2: [-5, 0], 3: [6, -1], 4: [-5, 0], 5: [-4, 0], 6: [10, 0], 7: [0, 9], 8: [9, -5], 9: [2, -3]}

CHOISE_ADD_COMPLEX_NUMBER=1
CHOISE_PRINT_COMPLEX_NUMBERLIST=2
CHOISE_FIND_LENGHT_AND_ELEMENTS_OF_LONGEST_SUBARRAY=3
CHOISE_FIND_LENGHT_AND_ELEMENTS_OF_LONGEST_INCREASING_SUBSEQUENCE_BASED_ON_MODULE=4
CHOISE_EXIT=5

while True:
    print("1. Add a complex number -> z=a+bi")
    print("2. Print the list with complex numbers")
    print("3. Find the length and elements of a longest subarray of distinct numbers")
    print("4. Find the length and elements of a longest increasing subsequence, when considering each number's modulus")
    print("5. EXIT")

    command = int(input("Input a command -> "))

    if command == CHOISE_ADD_COMPLEX_NUMBER:
        input_number(complex_numberlist)
    elif command == CHOISE_PRINT_COMPLEX_NUMBERLIST:
        print_numberlists(complex_numberlist)
    elif command == CHOISE_FIND_LENGHT_AND_ELEMENTS_OF_LONGEST_SUBARRAY:
        length_and_elements_of_a_longest_subarray_of_distinct_numbers(complex_numberlist)
    elif command == CHOISE_FIND_LENGHT_AND_ELEMENTS_OF_LONGEST_INCREASING_SUBSEQUENCE_BASED_ON_MODULE:
        the_length_and_elements_of_a_longest_increasing_subsequence_when_considering_each_number_s_modulus(complex_numberlist)
    elif command == CHOISE_EXIT:
        print("You stopped the program...")
        break
    else:
        print("The command you input isn't valid, please input another command...")
