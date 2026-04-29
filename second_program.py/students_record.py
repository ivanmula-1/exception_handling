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


    return student_records

def analyze_top_performer(records):
    """Determines the student with the best GWA (closest to 1.0) and displays results."""
    if not records:
        print("No valid student records found to analyze.")
        return

 top_student = min(records, key=lambda student: student['gwa'])

    print("=" * 40)
    print("       ACADEMIC EXCELLENCE REPORT")
    print("=" * 40)
    print(f"Total Students Processed: {len(records)}")
    print("-" * 40)
    print(f"Top Performer: {top_student['name']}")
    print(f"Highest GWA:   {top_student['gwa']:.2f} (Top of the Class)")
    print("=" * 40)

def main():
    filename = 'students.txt'
    data = get_student_data(filename)
    if data:
        analyze_top_performer(data)

if __name__ == "__main__":
    main()
