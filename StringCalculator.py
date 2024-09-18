def add(input_string):
    
    if input_string == "":
        return 0
    elif input_string == "0":
        return 0
    return None 


    
    # Handle custom delimiters
    if input_string.startswith("//"):
        delimiter, input_string = input_string[2:].split("\n", 1)
        numbers = input_string.split(delimiter)
    else:
        numbers = input_string.replace("\n", ",").split(",")

    # Convert numbers to integers and filter out those greater than 1000
    numbers = [int(num) for num in numbers if int(num) <= 1000]

    return sum(numbers)  # Return the sum of the valid numbers

