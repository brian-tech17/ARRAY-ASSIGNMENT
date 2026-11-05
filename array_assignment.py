# DATA STRUCTURES AND ALGORITHMS
# ARRAY CREATION

# Creating an array of five elements
my_array = [10, 20, 30, 40, 50]

# Displaying the array
print("Original Array:", my_array)
# INSERTING A VALUE INTO AN ARRAY

value = int(input("Enter the value to insert: "))
position = int(input("Enter the position to insert: "))

if 0 <= position <= len(my_array):

    my_array.append(0)

    for i in range(len(my_array) - 1, position, -1):
        my_array[i] = my_array[i - 1]

    my_array[position] = value

    print("Array after insertion:", my_array)

else:
    print("Invalid position")
    # DELETING A VALUE FROM AN ARRAY

delete_value = int(input("Enter the value to delete: "))

if delete_value in my_array:

    position = my_array.index(delete_value)

    for i in range(position, len(my_array) - 1):
        my_array[i] = my_array[i + 1]

    my_array.pop()

    print("Array after deletion:", my_array)

else:
    print("Value not found in the array")


# DISPLAY FINAL ARRAY
print("Final Array:", my_array)