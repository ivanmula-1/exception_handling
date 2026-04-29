def process_integers(input_filename):
    try:
        with open(input_filename, 'r') as source_file:
            numbers = [int(line.strip()) for line in source_file if line.strip()]

with open('double.txt', 'w') as double_file, open('triple.txt', 'w') as triple_file:
