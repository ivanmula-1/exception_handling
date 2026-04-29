def split_numbers(input_file):
    try:
        with open(input_file, 'r') as f:

            numbers = [int(line.strip()) for line in f if line.strip()]

evens = [str(n) for n in numbers if n % 2 == 0]
        odds = [str(n) for n in numbers if n % 2 != 0]

  with open('even.txt', 'w') as ef:
            ef.write('\n'.join(evens))

        with open('odd.txt', 'w') as of:
            of.write('\n'.join(odds))

        print("Files 'even.txt' and 'odd.txt' created successfully.")

 except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except ValueError:
        print("Error: Ensure the file contains only integers.")
