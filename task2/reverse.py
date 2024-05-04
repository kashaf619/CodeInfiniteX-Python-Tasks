def reverse_string(input_string):
    # Convert the string to a list of characters
    char_list = list(input_string)
    
    # Initialize pointers for the start and end of the list
    start = 0
    end = len(char_list) - 1
    
    # Loop until the pointers meet
    while start < end:
        # Swap characters at the start and end positions
        char_list[start], char_list[end] = char_list[end], char_list[start]
        
        # Move the pointers towards the center
        start += 1
        end -= 1
    
    # Convert the list of characters back to a string
    reversed_string = ''.join(char_list)
    
    return reversed_string

def main():
    input_str = input("Enter a string to reverse: ")
    reversed_str = reverse_string(input_str)
    print("Reversed string:", reversed_str)

if __name__ == "__main__":
    main()
