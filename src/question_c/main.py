#add import
from src.question_c.question_c import get_stock_list, display_stock_list

def main():
    keep_going = 'y'
    while keep_going.lower() == 'y':
        current_stock_list = get_stock_list()

        print('\n----- Stock Menu -----')
        print('1 - Display stock purchase history')
        print('2 - Exit')
        print('---------------')

        try:
            choice = int(input('Enter your choice:'))
            while choice < 1 or choice > 2:
                print('Invalid, please try again.')
                break

            if choice == 1:
                display_stock_list(current_stock_list)

            elif choice == 2:
                keep_going = 'n'
        except ValueError:
            print("Invalid input, please try again. ")
    print("\nExiting program.")

if __name__ == '__main__':
    main()