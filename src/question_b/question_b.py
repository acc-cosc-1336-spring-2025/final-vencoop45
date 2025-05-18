#write functions here, don't add input('') statements here!

def create_multiplication_table():
    table = []
    for row_num in range(1, 6):
        current_row = []
        for col_num in range(1, 11):
            value = row_num * col_num
            current_row.append(value)
        table.append(current_row)
    return table

def display_multiplication_table(table_list):
    for row in table_list:
        for element in row:
            print(f'{element}\t', end='')
        print()