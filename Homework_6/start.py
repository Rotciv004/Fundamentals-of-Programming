from ui import (
    get_user_input, display_error, display_result
)
from functions import ( add_complex_number_at_position, remove_complex_number_at_position, remove_sequence_of_complex_numbers, replace_old_value_if_exists, display_complex_numbers_between_positions, display_complex_number_list,
display_complex_numbers_with_modulus_comparison_equal_than_a_value,display_complex_numbers_with_modulus_comparison_greater_than_a_value, display_complex_numbers_with_modulus_comparison_less_than_a_value,
filter_complex_numbers_with_modulus_comparison_equal_than_a_value,filter_complex_numbers_with_modulus_comparison_greater_than_a_value,filter_complex_numbers_with_modulus_comparison_less_than_a_value,filter_complex_numbers_after_real_part,
undo
)

ADD_COMPLEX_NUMBER = "add"
INSERT = "insert"
LIST = "list"
UNDO = "undo"
EXIT = "exit"

INSERT_COMMAND=0
REMOVE_COMMAND=0
ADD_COMMAND = 0
REPLACE_COMMAND =0
LIST_COMMAND = 0
FILTER_REAL_POZITION = 0

CONDITION_COMMAND = 2
NUMBER_COMMADN = 3
NUMBER_TO_ADD = 1
POSITION_NUMBER_TO_ADD = 3
POSITION_NUMBER_TO_REMOVE = 1
START_POSITION_VALUE = 1
END_POSITION_VALEU = 3
OLD_VALUE_POSITION = 1
NEW_VALUE_POSITION = 3
START_POSITION_LIST_VALUE = 2
END_POSITION_LIST_VALEU = 4
SIGN_POSITION = 2

LIST_THE_COMPLEX_NUMBER_LIST = 1
LIST_A_SEQUENCE_FOR_COMPLEX_NUMBER_LIST = 5
REMOVE_A_NUMBER_FROM_A_POSITION = 2

REMOVE = "remove"
REPLACE= "replace"

FILTER_REAL = "filter"

while True:

    complex_numberdictionary = {0: [1, 2], 1: [-1, 0], 2: [3, -5], 3: [10, -12], 4: [-9, -3], 5: [0, -4], 6: [0, 1],
                                7: [9, 5], 8: [3, 0], 9: [0, -6]}
    complex_number_stack = []

    while True:

        command = str(get_user_input())
        command.lower()

        command_list=command.split(" ")

        if command_list[ADD_COMMAND] == ADD_COMPLEX_NUMBER:
            complex_number = command_list[NUMBER_TO_ADD]
            position = -1
            add_complex_number_at_position(complex_number, position,complex_numberdictionary,complex_number_stack)

        elif command_list[INSERT_COMMAND] == INSERT:
            complex_number = command_list[NUMBER_TO_ADD]
            position = int(command_list[POSITION_NUMBER_TO_ADD])
            add_complex_number_at_position(complex_number, position,complex_numberdictionary,complex_number_stack)

        elif command_list[REMOVE_COMMAND] == REMOVE:
            if len(command_list) == REMOVE_A_NUMBER_FROM_A_POSITION:
                position = int(command_list[POSITION_NUMBER_TO_REMOVE])
                remove_complex_number_at_position(position,complex_numberdictionary,complex_number_stack)
            else:
                start_position = int(command_list[START_POSITION_VALUE])
                end_position = int(command_list[END_POSITION_VALEU])
                remove_sequence_of_complex_numbers(start_position, end_position,complex_numberdictionary,complex_number_stack)

        elif command_list[REPLACE_COMMAND] == REPLACE:
            old_value = command_list[OLD_VALUE_POSITION]
            new_value = command_list[NEW_VALUE_POSITION]
            replace_old_value_if_exists(old_value, new_value,complex_numberdictionary,complex_number_stack)

        elif command_list[LIST_COMMAND] == LIST:
            if len(command_list) == LIST_THE_COMPLEX_NUMBER_LIST:
                display_complex_number_list(complex_numberdictionary)
            elif len(command_list) == LIST_A_SEQUENCE_FOR_COMPLEX_NUMBER_LIST:
                start_position = int(command_list[START_POSITION_LIST_VALUE])
                end_position = int(command_list[END_POSITION_LIST_VALEU])
                display_complex_numbers_between_positions(start_position, end_position,complex_numberdictionary)
            else:
                if command_list[CONDITION_COMMAND] == ">":
                    value = int(command_list[NUMBER_COMMADN])
                    display_complex_numbers_with_modulus_comparison_greater_than_a_value(value,complex_numberdictionary)
                elif command_list[CONDITION_COMMAND] == "<":
                    value = int(command_list[NUMBER_COMMADN])
                    display_complex_numbers_with_modulus_comparison_less_than_a_value(value,complex_numberdictionary)
                elif command_list[CONDITION_COMMAND] == "=":
                    value = int(command_list[NUMBER_COMMADN])
                    display_complex_numbers_with_modulus_comparison_equal_than_a_value(value,complex_numberdictionary)

        elif command_list[FILTER_REAL_POZITION] == FILTER_REAL:
            if len(command_list) == SIGN_POSITION:
                filter_complex_numbers_after_real_part(complex_numberdictionary,complex_number_stack)
            else:
                if command_list[CONDITION_COMMAND] == ">":
                    value = int(command_list[NUMBER_COMMADN])
                    filter_complex_numbers_with_modulus_comparison_greater_than_a_value(value,complex_numberdictionary,complex_number_stack)
                elif command_list[CONDITION_COMMAND] == "<":
                    value = int(command_list[NUMBER_COMMADN])
                    filter_complex_numbers_with_modulus_comparison_less_than_a_value(value,complex_numberdictionary,complex_number_stack)
                elif command_list[CONDITION_COMMAND] == "=":
                    value = int(command_list[NUMBER_COMMADN])
                    filter_complex_numbers_with_modulus_comparison_equal_than_a_value(value,complex_numberdictionary,complex_number_stack)

        elif command == UNDO:
            undo(complex_numberdictionary,complex_number_stack)

        elif command == EXIT:
            display_result("Exiting the program")
            break

        else:
            display_error(f"Invalid command, {command}. Please retry!")

    break



