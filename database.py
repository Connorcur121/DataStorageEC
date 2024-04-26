#Connor Curcio
#Database Storage Extra Credit Assignment CIS 4930
class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction_in_progress = False
        self.transaction_data = {}

    def get(self, key):
        return self.data.get(key, None)

    def put(self, key, val):
        if not self.transaction_in_progress:
            raise Exception("Transaction not in progress")
        self.transaction_data[key] = val

    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Transaction already in progress")
        self.transaction_in_progress = True

    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("No open transaction to commit")
        self.data.update(self.transaction_data)
        self.transaction_in_progress = False
        self.transaction_data = {}

    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("No ongoing transaction to rollback")
        self.transaction_in_progress = False
        self.transaction_data = {}


def print_menu():
    print("1. Get value by key")
    print("2. Put value by key")
    print("3. Begin transaction")
    print("4. Commit transaction")
    print("5. Rollback transaction")
    print("6. Exit")


def main():
    inmemoryDB = InMemoryDB()

    while True:
        print("\n--- Menu ---")
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            print("Value:", inmemoryDB.get(key))
        elif choice == "2":
            key = input("Enter key: ")
            try:
                val = int(input("Enter value: "))
                inmemoryDB.put(key, val)
            except ValueError:
                print("Error: Must be integer for value")
            except Exception as error:
                print("Error:", error)
        elif choice == "3":
            try:
                inmemoryDB.begin_transaction()
                print("Transaction started")
            except Exception as error:
                print("Error:", error)
        elif choice == "4":
            try:
                inmemoryDB.commit()
                print("Transaction committed")
            except Exception as error:
                print("Error:", error)
        elif choice == "5":
            try:
                inmemoryDB.rollback()
                print("Transaction rolled back")
            except Exception as error:
                print("Error:", error)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
