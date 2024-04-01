def generate_ascii_table(class_counts, total_rows, percentages):
    table = f"+{'-' * 30}+{'-' * 15}+{'-' * 15}+{'-' * 15}+\n"
    table += f"|{'Class':^30}|{'Count':^15}|{'Percentage':^15}|{'Total Rows':^15}|\n"
    table += f"+{'-' * 30}+{'-' * 15}+{'-' * 15}+{'-' * 15}+\n"

    for class_label, count in class_counts.items():
        percentage = percentages[class_label]
        table += f"|{class_label.capitalize():^30}|{count:^15}|{percentage:.2f}%{' ':>8}|{total_rows:^15}|\n"

    table += f"+{'-' * 30}+{'-' * 15}+{'-' * 15}+{'-' * 15}+\n"

    return table

def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def count_class_and_row(data):
    class_count = {}
    total_row = len(data) - 1  
    for row in data[1:]:  
        class_label = row[-1]
        if class_label in class_count:
            class_count[class_label] += 1
        else:
            class_count[class_label] = 1

    return class_count, total_row

def calculate_percentage(counts, total_row):
    percentages = {class_label: (count / total_row) * 100 for class_label, count in counts.items()}
    return percentages


diabetes_data = read_csv('../data/diabetes.csv')
soybean_data = read_csv('../data/soybean.csv')


diabetes_class_count, diabetes_total_row = count_class_and_row(diabetes_data)
soybean_class_count, soybean_total_row = count_class_and_row(soybean_data)


diabetes_percentages = calculate_percentage(diabetes_class_count, diabetes_total_row)
soybean_percentages = calculate_percentage(soybean_class_count, soybean_total_row)


diabetes_table = generate_ascii_table(diabetes_class_count, diabetes_total_row, diabetes_percentages)
soybean_table = generate_ascii_table(soybean_class_count, soybean_total_row, soybean_percentages)

with open('../w3/w3', 'w') as output_file:
    output_file.write("Diabetes Dataset:\n")
    output_file.write(diabetes_table)
    output_file.write("\nSoybean Dataset:\n")
    output_file.write(soybean_table)