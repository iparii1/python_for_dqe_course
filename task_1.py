import random


# Function to sort a list using Bubble Sort
def sort_list(my_list):
    # Iterate over the list for the required number of passes
    for n in range(len(my_list) - 1):
        # Set swapped flag to False at the start of each pass
        swapped = False
        # Perform comparisons in the unsorted portion of the list
        for i in range(len(my_list) - n - 1):
            # Check if the current item is greater than the next item
            if my_list[i] > my_list[i + 1]:
                # Swap the items if the condition is true
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                # Set 'swapped' flag to True after a swap
                swapped = True
        # If no swaps occurred during the pass, the list is sorted
        if not swapped:
            break
    # Return the sorted list
    return my_list


# Function to calculate the average of even numbers in a list
def average_of_even_numbers(my_list):
    count = 0
    total = 0
    # Iterate over each item in the list
    for i in my_list:
        # Check whether the item is even
        if i % 2 == 0:
            # Add item to the total
            total += i
            # Increase items count by 1
            count += 1
    # Return average
    return round(total / count, 2)


# Function to calculate the average of odd numbers in a list
def average_of_odd_numbers(my_list):
    count = 0
    total = 0
    # Iterate over each item in the list
    for i in my_list:
        # Check whether the item is odd
        if i % 2 != 0:
            # Add item to the total
            total += i
            # Increase items count by 1
            count += 1
    # Return average
    return round(total / count, 2)


if __name__ == '__main__':
    # Generate a list of 100 unique random values from 0 to 1000
    random_list = random.sample(range(0, 1000), 100)
    print('Unsorted ist:', random_list)

    # Sort the list using the sort_list function
    sorted_list = sort_list(random_list)
    print('Sorted list:', sorted_list)

    # Calculate average of even numbers in the list
    even_average = average_of_even_numbers(random_list)
    print('Average of even numbers:', even_average)

    # Calculate average of odd numbers in the list
    odd_average = average_of_odd_numbers(random_list)
    print('Average of odd numbers:', odd_average)
