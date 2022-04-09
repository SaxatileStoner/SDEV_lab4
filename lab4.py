"""
* Lab 4 - Week 4 Deliverables
* Building Secure Python Applications - SDEV 300
*
* @author Christopher Stoner
* 
* Consists of three main parts
* 1) Allows user to enter and validate their phone number and zipcode+4
        Then the user will enter values of two, 3 x 3 matrices and then select from options:
            a) Addition
            b) Subtraction
            c) Matrix Multiplication
            d) Element by element multiplication
        should use numpy.matmul() for matrix multiplcation
        should compute the appropriate results, and return results, 
            the transponse of the results, and the mean of the rows for the results,
            and the mean of the columns for the results

* 2) Document your testing results using your programming environment.
        Include and discuss your pylint results for the application.
        
* 3) Password cracker using Python code.
        
"""

import numpy as np
import re


def promt_y_n():
    """Runs through promts for yes or no, 
    returns capitalized letter Y or N.

    Returns:
        str: 'Y' or 'N'
    """
    print("Enter Y for Yes or N for No: \n")
    while True:
        try:
            ans = str(input("> ")).capitalize()
            if ans == 'Y' or ans == 'N':  # This is an acceptable answer
                return ans
            continue
        except TypeError:
            print("Exception thrown, TypeError!")
            continue


def to_3x3_matrix(row_1, row_2, row_3):
    """Takes strings that represent rows in a matrix, 
    converts each row into an array with .split, then
    returns a array object  

    Args:
        row_1 (str): Row 1 of Matrix
        row_2 (str): Row 2 of Matrix
        row_3 (str): Row 3 of Matrix

    Returns:
        numpy.array: returns object array from numpy lib
    """
    array_row_1 = np.array(row_1.split(), dtype=int)
    array_row_2 = np.array(row_2.split(), dtype=int)
    array_row_3 = np.array(row_3.split(), dtype=int)

    return np.mat([array_row_1, array_row_2, array_row_3])


def input_row():
    """Runs through promt to get and check if inputed data is 
    a row representing a matrix row

    Returns:
        str: returns a string of numbers seperated by a whitespace character
        This represents a row in a matrix
    """
    regex_row = "^\d+\s\d+\s\d+$"
    while True:
        try:
            row = str(input("> "))
            if re.match(regex_row, row):
                return row
            print("Not a valid row, try again:\n")
            continue
        except TypeError:
            print("Exception thrown, TypeError!")
            continue


def main():
    """Main function that runs the program
    """
    print("*********** Welcome to the Python Matrix Application ***********")
    # ---- PHONE NUMBER STARTS ---- #
    print("Would you like to continue?\n")
    ans = promt_y_n()
    if(ans == 'N'):
        return
    print("\nEnter your phone number (XXX-XXX-XXXX): ")
    while True:
        try:
            phone_num = str(input("> "))
            if(re.match("^\d{3}-\d{3}-\d{4}$", phone_num)):
                break
            print("\nNot a valid phone number. Renter: \n")
            continue
        except TypeError:
            print("Exception thrown, TypeError!")
            continue

    print("\nEnter Your zip code+4 (XXXXX-XXXX): ")
    while True:
        try:
            zip_code = str(input("> "))
            if(re.match("^\d{5}-\d{4}$", zip_code)):
                break
            print("\nNot a valid zip code. Renter: \n")
            continue
        except TypeError:
            print("Exception thrown, TypeError!")
            continue

    # ---- MATRIX STARTS ---- #
    while True:
        print("\nWould you like to calculate matrices?\n")
        ans = promt_y_n()
        if ans == 'N':
            return
        print("\nEnter your first 3x3 matrix one row at a time, each row seperated by an enter: \n")
        str_row_1 = input_row()
        str_row_2 = input_row()
        str_row_3 = input_row()

        matrix_1 = to_3x3_matrix(str_row_1, str_row_2, str_row_3)

        print("\nYour first 3x3 matrix is: \n")
        print(matrix_1)
        # Might make the print statement more user friendly,
        # but this is good enough for debugging

        print("\nEnter your second 3x3 matrix one row at a time, each row seperated by an enter: \n")
        str_row_1 = input_row()
        str_row_2 = input_row()
        str_row_3 = input_row()

        matrix_2 = to_3x3_matrix(str_row_1, str_row_2, str_row_3)
        print("\nYour second 3x3 matrix is: \n")
        print(matrix_2)

        # OPERATION ON MATRIX #
        valid_operators = ["A", "B", "C", "D"]
        print("\nSelect a Matrix Operation from the list below: \n")
        print("a. Addition\nb. Subtraction\nc. Matrix Multiplication\nd. Element by element multiplication\n")
        flag = True
        while flag:
            try:
                operation = str(input("> ")).capitalize()
                for op in valid_operators:
                    if op == operation:
                        flag = False
                        break
                if flag:
                    print("\nNot a valid option! Please try again: \n")
                    continue
            except TypeError:
                print("Exception thrown, TypeError!")
                continue

        # if...elif to make selection on what operation to do on the matrices
        if operation == "A":  # Matrix Addition
            result = matrix_1 + matrix_2
            print("\nYou have selected Addition. The results are: \n")
            print(result)
        elif operation == "B":  # Matrix Subtraction
            result = matrix_1 - matrix_2
            print("\nYou have selected Subtraction. The results are: \n")
            print(result)
        elif operation == "C":  # Matrix Multiplication
            result = np.matmul(matrix_1, matrix_2)
            print("\nYou have selected Matrix Multiplication. The results are: \n")
            print(result)
        elif operation == "D":  # Element by element multiplication
            result = np.multiply(matrix_1, matrix_2)
            print("\nYou have selected Element by element. The results are: \n")
            print(result)
        else:
            print("And error has occured!")
            return

        # Transpose the result
        print("\nThe transpose is: \n")
        print(np.transpose(result))

        print("\nThe row and column mean values of the results are: \n")

        row_mean = np.mean(result, axis=1)
        col_mean = np.mean(result, axis=0)

        row_mean = np.ndarray.flatten(row_mean)

        print(f"Row: {row_mean}")
        print(f"Col: {col_mean}")


if __name__ == '__main__':
    main()
