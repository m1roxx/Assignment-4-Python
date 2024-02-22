from database import Database
from smartphoneManager import SmartphoneManager


def menu():
    print("*** Welcome to Smartphone Manager! ***")
    print("1. Customer")
    print("2. Seller")
    print("3. Exit")


def customerMenu():
    print("Menu:")
    print("1. Show all Smartphones")
    print("2. Search by Smartphones")
    print("3. Rating of Smartphones")
    print("4. Exit")


def sellerMenu():
    print("Menu:")
    print("1. Show all Smartphones")
    print("2. Add Smartphone")
    print("3. Update Smartphone")
    print("4. Delete Smartphone")
    print("5. Rating of Smartphones")
    print("6. Exit")


def main():
    try:
        database = Database(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        database.connect()
        manager = SmartphoneManager(database.connection)

        menu()
        option = int(input("Enter your choice >> "))

        while True:

            if option == 1:
                customerMenu()
                choice = int(input("Choose an option >> "))

                if choice == 1:
                    manager.showAllSmartphones()

                elif choice == 2:
                    manager.searchSmartphone()

                elif choice == 3:
                    manager.ratingOfSmartphones()

                elif choice == 4:
                    print("Exiting program.")
                    break

                else:
                    print("Invalid choice. Please try again.")

            elif option == 2:
                sellerMenu()
                choice = int(input("Choose an option >> "))

                if choice == 1:
                    manager.showAllSmartphones()

                elif choice == 2:
                    manager.addSmartphone()

                elif choice == 3:
                    manager.updateSmartphone()

                elif choice == 4:
                    manager.deleteSmartphone()

                elif choice == 5:
                    manager.ratingOfSmartphones()

                elif choice == 6:
                    print("Exiting program.")
                    break

                else:
                    print("Invalid choice. Please try again.")

            elif option == 3:
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print("Error:", e)

    finally:
        if database is not None:
            database.disconnect()


if __name__ == "__main__":
    main()
