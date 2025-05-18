#add import

from src.question_b.question_b import create_multiplication_table, display_multiplication_table

def main():
    while True:
        multiplication_table = create_multiplication_table()
        display_multiplication_table(multiplication_table)

        keep_going = input('Do you want to generate another table? (y/n):').lower()
        if keep_going != 'y':
            break

if __name__ == "__main__":
    main()