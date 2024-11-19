import math

def input_number(real_numberlist:list,imaginar_numberlist:list):
    complex_number= input("Input a complex number ->")
    delete_i=complex_number.split("i")
    real=0
    imaginary=0

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

    real_numberlist.append(real)
    imaginar_numberlist.append(imaginary)

def print_numberlists(real_numberlist:list,imaginar_numberlist:list):
    for index in range(len(real_numberlist)):
        if imaginar_numberlist[index] != 0 and real_numberlist[index] != 0:
            if imaginar_numberlist[index] > 0:
                print("C[" + str(index) + "]= " + str(real_numberlist[index]) + "+" + str(imaginar_numberlist[index]) + "i")
            else:
                print("C[" + str(index) + "]= " + str(real_numberlist[index]) + str(imaginar_numberlist[index]) + "i")

        elif imaginar_numberlist[index] == 0 and real_numberlist[index] != 0:
                print("C[" + str(index) + "]= " + str(real_numberlist[index]))

        elif real_numberlist[index] == 0 and imaginar_numberlist[index] != 0:
                print("C[" + str(index) + "]= " + str(imaginar_numberlist[index]) + "i")

        else:
            print("C[" + str(index) + "]= 0")


def remove_elements_from_max_numberlists(real_numberlist:list,imaginar_numberlist:list):
    while len(real_numberlist)>0:
        real_numberlist.pop()
        imaginar_numberlist.pop()

def add_elements_to_max_numberlists(left:int,right:int,real_numberlist:list,imaginar_numberlist:list,max_real_numberlist:list, max_imaginar_numberlist:list):
    for index in range(left,right):
        max_real_numberlist.append(real_numberlist[index])
        max_imaginar_numberlist.append((imaginar_numberlist[index]))


def modul_of_complex_numbers(real:int,imaginar:int)->float:
    return math.sqrt(real**2+imaginar**2)


def the_length_and_elements_of_a_longest_increasing_subsequence_when_considering_each_number_s_modulus(real_numberlist:list,imaginar_numberlist:list):
    max_real_numberlist=[]
    max_imaginar_numberlist=[]

    index_left = 0

    for index_right in range(0, len(real_numberlist)):
        if modul_of_complex_numbers(real_numberlist[index_right],imaginar_numberlist[index_right]) < modul_of_complex_numbers(real_numberlist[index_right-1],imaginar_numberlist[index_right-1]):
            if len(max_real_numberlist) < index_right - index_left + 1:
                remove_elements_from_max_numberlists(max_real_numberlist, max_imaginar_numberlist)
                add_elements_to_max_numberlists(index_left, index_right, real_numberlist, imaginar_numberlist,max_real_numberlist, max_imaginar_numberlist)

            index_left = index_right

    if len(max_real_numberlist) < len(real_numberlist) - index_left:
        remove_elements_from_max_numberlists(max_real_numberlist, max_imaginar_numberlist)
        add_elements_to_max_numberlists(index_left, len(real_numberlist)-1, real_numberlist, imaginar_numberlist,max_real_numberlist, max_imaginar_numberlist)

    print_numberlists(max_real_numberlist, max_imaginar_numberlist)
    print(len(max_real_numberlist))


def verify_if_a_number_is_alredy_in_the_max_numberlist(real:int,imaginar:int,left:int,right:int,real_numberlist:list,imaginar_numberlist)->bool:
    for index in range(left,right):
        if real == real_numberlist[index] and imaginar == imaginar_numberlist[index]:
            return True

    return False

def length_and_elements_of_a_longest_subarray_of_distinct_numbers(real_numberlist:list, imaginar_numberlist:list):
    max_real_numberlist = []
    max_imaginar_numberlist = []
    index_left=0

    for index_right in range(0,len(real_numberlist)):
        if verify_if_a_number_is_alredy_in_the_max_numberlist(real_numberlist[index_right] , imaginar_numberlist[index_right] , index_left , index_right , real_numberlist , imaginar_numberlist):
            if len(max_real_numberlist)<index_right-index_left+1:
                remove_elements_from_max_numberlists(max_real_numberlist,max_imaginar_numberlist)
                add_elements_to_max_numberlists(index_left,index_right,real_numberlist, imaginar_numberlist,max_real_numberlist,max_imaginar_numberlist)

            index_left=index_right

    if len(max_real_numberlist) < len(real_numberlist) - index_left:
        remove_elements_from_max_numberlists(max_real_numberlist, max_imaginar_numberlist)
        add_elements_to_max_numberlists(index_left, len(real_numberlist)-1, real_numberlist, imaginar_numberlist,max_real_numberlist, max_imaginar_numberlist)

    print_numberlists(max_real_numberlist,max_imaginar_numberlist)
    print(len(max_real_numberlist))



real_numberlist=[1,3,-5,6,-5,-4,10,0,9,2]
imaginar_numberlist=[12,10,0,-1,0,0,0,9,-5,-3,2]

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

    command=int(input("Input a command -> "))

    if command== CHOISE_ADD_COMPLEX_NUMBER:
       input_number(real_numberlist,imaginar_numberlist)

    elif command== CHOISE_PRINT_COMPLEX_NUMBERLIST:
        print_numberlists(real_numberlist,imaginar_numberlist)

    elif command== CHOISE_FIND_LENGHT_AND_ELEMENTS_OF_LONGEST_SUBARRAY:
        length_and_elements_of_a_longest_subarray_of_distinct_numbers(real_numberlist,imaginar_numberlist)

    elif command== CHOISE_FIND_LENGHT_AND_ELEMENTS_OF_LONGEST_INCREASING_SUBSEQUENCE_BASED_ON_MODULE:
        the_length_and_elements_of_a_longest_increasing_subsequence_when_considering_each_number_s_modulus(real_numberlist,imaginar_numberlist)

    elif command== CHOISE_EXIT:
        print("You stop the program...")
        break

    else:
        print("The command do you input isn't valide, please input another command...")

