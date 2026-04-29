def split_numbers(input_file):
    try:
        with open(input_file, 'r') as f:

            numbers = [int(line.strip()) for line in f if line.strip()]

evens = [str(n) for n in numbers if n % 2 == 0]
        odds = [str(n) for n in numbers if n % 2 != 0]
