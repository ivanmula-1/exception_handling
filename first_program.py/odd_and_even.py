def split_numbers(input_file):
    try:
        with open(input_file, 'r') as f:

            numbers = [int(line.strip()) for line in f if line.strip()]
