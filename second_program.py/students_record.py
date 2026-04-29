import os

def get_student_data(filepath):
    """Reads file and returns a list of dictionaries for better data handling."""
    student_records = []
    
    if not os.path.exists(filepath):
        print(f"Critical Error: The file '{filepath}' was not found.")
        return None

    with open(filepath, 'r') as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue

            try:
                name, gwa_str = line.split(',')
                record = {
                    'name': name.strip(),
                    'gwa': float(gwa_str.strip())
                }
                student_records.append(record)
            except ValueError:
                print(f"Skipping line {line_number}: Invalid format or GWA value.")
