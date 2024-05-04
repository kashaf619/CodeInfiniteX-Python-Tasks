import csv

def analyze_csv(csv_file, column_name):
    # Initialize variables for calculations
    total = 0
    count = 0
    max_value = float('-inf')
    min_value = float('inf')

    # Read data from CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                value = float(row[column_name])
                total += value
                count += 1
                if value > max_value:
                    max_value = value
                if value < min_value:
                    min_value = value
            except ValueError:
                print(f"Error: Invalid value '{row[column_name]}' in row {reader.line_num}")

    # Calculate average
    if count > 0:
        average = total / count
        return {
            'average': average,
            'maximum': max_value,
            'minimum': min_value
        }
    else:
        return None

def main():
    csv_file = "C:/Users/Dell/Desktop/python/task3/sample.csv" # CSV file path
    column_name = "value"     # Column to be analyzed

    # Perform analysis
    analysis_result = analyze_csv(csv_file, column_name)

    # Display results
    if analysis_result:
        print("Analysis Results:")
        print(f"Average {column_name}: {analysis_result['average']}")
        print(f"Maximum {column_name}: {analysis_result['maximum']}")
        print(f"Minimum {column_name}: {analysis_result['minimum']}")
    else:
        print("No data found in the specified column.")

if __name__ == "__main__":
    main()
