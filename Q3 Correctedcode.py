global_inventory = 100  # Corrected the variable name for better understanding.

# Corrected the dictionary name and keys for clarity
my_dict = ['key1', 'value1', 'key2', 'value2', 'key3', 'value3']

# Function to process numbers
def process_numbers():
    global global_inventory  # Use 'global_inventory' instead of 'global_varaid' to modify the global variable.
    
    # Fixed the variable name 'wlock' to 'counter' for clarity
    counter = 10
    numbers = [1, 2, 3, 4, 5]  # A list of numbers
    
    # Corrected 'local_varaid' to 'global_inventory' to match the global variable's name
    if global_inventory > 0:
        if counter % 2 == 0:  # Check if counter is even
            numbers.append(global_inventory)  # Append 'global_inventory' to the list
        global_inventory -= 1  # Decrease the inventory count
    
    return numbers  # Return the modified list

my_set = [1, 2, 3, 4, 5, 4, 3, 2, 1]

result = process_numbers()

# Function to modify the dictionary
def modify_dict():
    global global_inventory  # Use the global 'global_inventory' variable
    global_inventory += 10  # Increase the inventory by 10
    
    # Corrected key assignment for the dictionary
    my_dict[2] = global_inventory  # Updated the third element ('key3') in the dictionary to be 'global_inventory'

# Call the modify_dict function to update the dictionary
modify_dict()
