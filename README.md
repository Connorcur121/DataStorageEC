Welcome to a basic database transaction software to manage and store your transaction reports.

Instructions:

To start the program please clone the repository.
Open the terminal and change your working directory to the DataStorageEC folder
then use Python database.py to run the program

When the program starts you will be given a menu of 6 options
--- Menu ---
1. Get value by key
2. Put value by key
3. Begin transaction
4. Commit transaction
5. Rollback transaction
6. Exit
Enter your choice:

To begin a transaction you must enter 3 to begin transaction this will allow for transaction reports to be put into the database
after you confirm that a transaction has begun you can now enter 2 to put a new transaction into the database
the program will ask for a string(key), integer(val) pair then bring you back to the menu
if you wish to change the value you put it simply choose put value by key and re-enter your new value
if you wish to delete the transaction you made choose Rollback transaction by entering 5
this will delete any changes you have made within the current transaction and end the transaction

Committing to the database is simple.
After beginning a transaction and entering a transaction to the database using Put value by key
use Commit transaction to save your transaction to the database
After you commit any changes you can now use Get value by key to search the database for the transaction of your choice

Transactions will not be visible until you commit them to the database.


Assignment Modifications:
For this assignment to become "official" it would likely need some more complexity added to the program requirements.
Instead of a simple program that stores a database while the program is running, instead
make a real program that can store database information in a separate file then you can
open and close the program to enter transactions as you would with any other software.
adding extra complexity to other functions such as creating a table of transactions for keys
instead of only storing the last value committed per key.

Maybe adding a verification method to the assignment with security features could be interesting to learn.

