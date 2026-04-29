def write_multiple_lines():
    """Asks for user input and writes each line to mylife.txt."""
    try:
        with open('mylife.txt', 'w') as file:
            while True:
                # Ask the user for the text content
                line = input("Enter line: ")

 file.write(line + "\n")

        more_lines = input("Are there more lines y/n? ").lower()

 if more_lines != 'y':
                    break

        print("\nSuccess! Content has been saved to 'mylife.txt'.")

    except IOError:
        print("An error occurred while writing to the file.")

if __name__ == "__main__":
    write_multiple_lines()
