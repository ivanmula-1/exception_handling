def write_multiple_lines():
    """Asks for user input and writes each line to mylife.txt."""
    try:
        with open('mylife.txt', 'w') as file:
            while True:
                # Ask the user for the text content
                line = input("Enter line: ")
