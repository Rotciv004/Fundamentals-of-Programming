import math
import copy
from ui import display_error


def display_a_complex_number_after_index(index:int,complex_numberdictionary):
    REAL_PART = 0
    IMAGINARY_PART = 1
    if complex_numberdictionary[index][IMAGINARY_PART] != 0:
        sign = "+" if complex_numberdictionary[index][IMAGINARY_PART] > 0 else ""
        print(f"C[{index}] = {complex_numberdictionary[index][REAL_PART]} {sign} {complex_numberdictionary[index][IMAGINARY_PART]}i")

    else:
        print(f"C[{index}] = {complex_numberdictionary[index][0]}")

def save_state(complex_numberdictionary,complex_number_stack):
    complex_number_stack.append(copy.deepcopy(complex_numberdictionary))


def modul_of_a_complex_number(real_part: int, imaginary_part: int) -> float:
    return math.sqrt(real_part ** 2 + imaginary_part ** 2)


def convert_an_input_value(complex_number):
    REAL_PART_POSITION = 0
    SIGN_POSITION = 1
    IMAGINARY_PART_POSITION = 2
    LEN_COMPLEX_NUMEBR = 3
    LEN_COMPLEX_NUMEBR_WHITOUT_A_PART = 2
    delete_i = complex_number.split("i")
    real = 0
    imaginary = 0

    if "+" in delete_i[REAL_PART_POSITION]:
        numbers = delete_i[REAL_PART_POSITION].split("+")
        if len(numbers) == LEN_COMPLEX_NUMEBR_WHITOUT_A_PART:
            real, imaginary = map(int, numbers)
        else:
            display_error("Invalid input")
    elif "-" in delete_i[REAL_PART_POSITION]:
        numbers = delete_i[REAL_PART_POSITION].split("-")
        if len(numbers) == LEN_COMPLEX_NUMEBR and numbers[REAL_PART_POSITION] == "":
            real, imaginary = -int(numbers[SIGN_POSITION]), -int(numbers[IMAGINARY_PART_POSITION])
        elif len(numbers) == LEN_COMPLEX_NUMEBR_WHITOUT_A_PART:
            real, imaginary = map(int, numbers)
    else:
        display_error("Invalid input")

    return real, imaginary


def verify_if_value_exists_in_complex_numberdict(complex_number, index_complex_number,complex_numberdictionary)->bool:
    REAL_PART = 0
    IMAGINARY_PART = 1
    real_part, imaginary_part = convert_an_input_value(complex_number)

    for index in range(0, len(complex_numberdictionary)):
        if complex_numberdictionary[index][REAL_PART] == real_part and complex_numberdictionary[index][IMAGINARY_PART] == imaginary_part:
            index_complex_number = index
            return True

    return False


def add_complex_number_at_position(complex_number, position,complex_numberdictionary,complex_number_stack):
    save_state(complex_numberdictionary,complex_number_stack)

    real, imaginary = convert_an_input_value(complex_number)

    if position == -1:
        complex_numberdictionary[len(complex_numberdictionary)] = [real, imaginary]

    elif 0 <= position < len(complex_numberdictionary):
        complex_numberdictionary[position] = [real, imaginary]

    else:
        display_error(f"The position {position} is not valid. Please retry!")


def remove_complex_number_at_position(position,complex_numberdictionary,complex_number_stack):
    REAL_PART = 0
    IMAGINARY_PART = 1
    save_state(complex_numberdictionary,complex_number_stack)

    if 0 <= position < len(complex_numberdictionary):
        for index in range(position, len(complex_numberdictionary) - 1):
            complex_numberdictionary[index][REAL_PART] = complex_numberdictionary[index + 1][REAL_PART]
            complex_numberdictionary[index][IMAGINARY_PART] = complex_numberdictionary[index + 1][IMAGINARY_PART]

        complex_numberdictionary.popitem()

    else:
        display_error(f"Your position, {position}, is invalid. Please retry")


def remove_sequence_of_complex_numbers(start_position, end_position,complex_numberdictionary,complex_number_stack):
    save_state(complex_numberdictionary,complex_number_stack)

    REAL_PART = 0
    IMAGINARY_PART = 1

    if 0 <= start_position <= end_position < len(complex_numberdictionary):
        for _ in range(start_position, end_position + 1):
            for index in range(start_position, len(complex_numberdictionary) - 1):
                complex_numberdictionary[index][REAL_PART] = complex_numberdictionary[index + 1][REAL_PART]
                complex_numberdictionary[index][IMAGINARY_PART] = complex_numberdictionary[index + 1][IMAGINARY_PART]

            complex_numberdictionary.popitem()

    else:
        display_error(f"Your positions, {start_position} and {end_position}, are invalid. Please retry")


def replace_old_value_if_exists(old_value, new_value,complex_numberdictionary,complex_number_stack):
    save_state(complex_numberdictionary,complex_number_stack)

    index = 0

    if verify_if_value_exists_in_complex_numberdict(old_value, index,complex_numberdictionary):
        real_part, imaginary_part = convert_an_input_value(new_value)
        complex_numberdictionary[index] = [real_part, imaginary_part]

    else:
        display_error(f"Your old value {old_value} doesn't exist in complex_numberdict. Please retry!")


def display_complex_numbers_between_positions(start_position, end_position,complex_numberdictionary):
    if 0 <= start_position <= end_position < len(complex_numberdictionary):
        for index in range(start_position, end_position + 1):
            display_a_complex_number_after_index(index,complex_numberdictionary)


    else:
        display_error("Invalid positions for display")


def display_complex_number_list(complex_numberdictionary):
    for index in range(0, len(complex_numberdictionary)):
            display_a_complex_number_after_index(index,complex_numberdictionary)


def display_complex_numbers_with_modulus_comparison_greater_than_a_value(value:int,complex_numberdictionary):
    for index in range(0, len(complex_numberdictionary)):
        if modul_of_a_complex_number(complex_numberdictionary[index][0], complex_numberdictionary[index][1]) > value:
            display_a_complex_number_after_index(index,complex_numberdictionary)


def display_complex_numbers_with_modulus_comparison_less_than_a_value(value: int,complex_numberdictionary):
    for index in range(0, len(complex_numberdictionary)):
        if modul_of_a_complex_number(complex_numberdictionary[index][0], complex_numberdictionary[index][1]) < value:
            display_a_complex_number_after_index(index,complex_numberdictionary)


def display_complex_numbers_with_modulus_comparison_equal_than_a_value(value: int,complex_numberdictionary):
    for index in range(0, len(complex_numberdictionary)):
        if modul_of_a_complex_number(complex_numberdictionary[index][0], complex_numberdictionary[index][1]) == value:
            display_a_complex_number_after_index(index,complex_numberdictionary)


def filter_complex_numbers_after_real_part(complex_numberdictionary,complex_number_stack):
    IMAGINARY_PART = 1
    REAL_PART = 0
    save_state(complex_numberdictionary,complex_number_stack)

    index = 0

    while index < len(complex_numberdictionary):
        if complex_numberdictionary[index][IMAGINARY_PART] != 0:
            for index_list in range(index, len(complex_numberdictionary) - 1):
                complex_numberdictionary[index_list][REAL_PART] = complex_numberdictionary[index_list + 1][REAL_PART]
                complex_numberdictionary[index_list][IMAGINARY_PART] = complex_numberdictionary[index_list + 1][IMAGINARY_PART]

            complex_numberdictionary.popitem()

        else:
            index = index + 1


def filter_complex_numbers_with_modulus_comparison_greater_than_a_value(value: int,complex_numberdictionary,complex_number_stack):
    REAL_PART = 0
    IMAGINARY_PART = 1
    save_state(complex_numberdictionary,complex_number_stack)

    index = 0

    while index < len(complex_numberdictionary):
        if modul_of_a_complex_number(complex_numberdictionary[index][REAL_PART], complex_numberdictionary[index][IMAGINARY_PART]) > value:
            for index_list in range(index, len(complex_numberdictionary) - 1):
                complex_numberdictionary[index_list][REAL_PART] = complex_numberdictionary[index_list + 1][REAL_PART]
                complex_numberdictionary[index_list][IMAGINARY_PART] = complex_numberdictionary[index_list + 1][IMAGINARY_PART]

            complex_numberdictionary.popitem()
        else:
            index= index + 1


def filter_complex_numbers_with_modulus_comparison_less_than_a_value(value: int,complex_numberdictionary,complex_number_stack):
    REAL_PART = 0
    IMAGINARY_PART = 1
    save_state(complex_numberdictionary,complex_number_stack)

    index =0

    while index < len(complex_numberdictionary):
        if modul_of_a_complex_number(complex_numberdictionary[index][REAL_PART], complex_numberdictionary[index][IMAGINARY_PART]) < value:
            for index_list in range(index, len(complex_numberdictionary) - 1):
                complex_numberdictionary[index_list][REAL_PART] = complex_numberdictionary[index_list + 1][REAL_PART]
                complex_numberdictionary[index_list][IMAGINARY_PART] = complex_numberdictionary[index_list + 1][IMAGINARY_PART]

            complex_numberdictionary.popitem()
        else:
            index = index + 1


def filter_complex_numbers_with_modulus_comparison_equal_than_a_value(value: int,complex_numberdictionary,complex_number_stack):
    REAL_PART = 0
    IMAGINARY_PART = 1
    save_state(complex_numberdictionary,complex_number_stack)

    index=0

    while index < len(complex_numberdictionary):
        if modul_of_a_complex_number(complex_numberdictionary[index][REAL_PART], complex_numberdictionary[index][IMAGINARY_PART]) == value:
            for index_list in range(index, len(complex_numberdictionary) - 1):
                complex_numberdictionary[index_list][REAL_PART] = complex_numberdictionary[index_list + 1][REAL_PART]
                complex_numberdictionary[index_list][IMAGINARY_PART] = complex_numberdictionary[index_list + 1][
                    IMAGINARY_PART]

            complex_numberdictionary.popitem()
        else:
            index = index + 1


def undo(complex_numberdictionary,complex_number_stack):
    if complex_number_stack:
        complex_numberdictionary.clear()
        complex_numberdictionary.update(complex_number_stack.pop())
    else:
        display_error("No more undo steps available.")