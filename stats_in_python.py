import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column

    # Get the filename for error messages
    filename = filepath.split("/")[-1]
    list_values = []
    # For total values in column, valid and invalid
    total_number_of_values = 0
    with open(filepath, "r") as file:
        for line in file:
            row_values = line.strip().split("\t")
            try:
                value = row_values[column]
                number = float(value)
                total_number_of_values += 1
                # Skip infinity values and NaN
                if math.isfinite(number):
                    list_values.append(number)
            except ValueError:
                pass
            except IndexError:
                print(f"Exiting: There is no valid \'list index\' in column {column} in line {total_number_of_values + 1} in file:{filename}")
                exit()
        
        # Exit if the list is empty
        if not list_values:
            print(f"Error: There were no valid number(s) in column {column} in file: {filename}")
            exit()

    return (list_values, float(total_number_of_values))


def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers

    return sum(numbers) / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order

    return (max(numbers), min(numbers))

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    
    n = len(numbers)
    # If there is only one value, the variance is 0
    if n == 1:
        return 0

    avg = calculate_average(numbers)
    sum_square_difference = 0
    # Get sum of the square difference
    for number in numbers:
        sum_square_difference += math.pow((number - avg),2)
    
    variance = sum_square_difference / (n - 1)
    return variance

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list

    # Standard deviation is the square root of the variance
    return math.sqrt(calculate_variance(numbers))

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    # Need to sort the variables in ascending order

    # Median is the center point of a sorted list
    # If the len of the list is odd, the center point is the length / 2
    # If the length is even, the median is the average of the two middle numbers

    n = len(number) 

    number.sort()
    median = 0

    if n % 2 == 1:
        median = float(number[n//2])
    else:
        right = number[n//2]
        left = number[n//2 - 1]
        median = (right + left) / 2
    return median