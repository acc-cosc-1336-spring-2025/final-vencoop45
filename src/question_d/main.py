#add import
from src.question_d.question_d import stock_purchase_history

def main():
    while True:
        print("\nMenu")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        try:
            choice = int(input("Please enter your choice:"))
            if choice == 1:
                stock_purchase_history()
            elif choice == 2:
                print("Exiting program")
            else:
                print("Invalid, please try again.")
        except ValueError:
            print("Invalid, please try again.")

if __name__ == '__main__':
    main()