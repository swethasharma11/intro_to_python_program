# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# Name: Swetha Sharma, Date: Feb 15th, 2021
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strFile = "ToDoToDOList.txt"

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have

objFile = open(objFileName, "w")
dicRow = {"Task": "Work", "Priority": "P1"}
objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
dicRow = {"Task": "Clean", "Priority": "P2"}
objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # File to List
        objFile = open(objFileName, "r")
        for row in objFile:
            line = row.split(",")
            lstTable.append(line) # Returns a list!
            print(line)
        objFile.close()
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("enter the new task")
        task = input()
        print("enter the priority")
        priority = input()
        new_list = [task, priority]
        lstTable.append(new_list)
        print(lstTable)
        for row in lstTable:
            print(row[0] + ',' + row[1])
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("here is the current list")
        print(lstTable)
        print("which item do you want to remove?")
        item = input()
        lstTable.remove("item")
        print(lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print(lstTable)
        objFile = open(strFile, "w")
        objFile.write(lstTable[0][0]+ ',' + lstTable[0][1] + '\n')
        objFile = open(strFile, "w")
        objFile.write(lstTable[1][0] + ',' + lstTable[1][1] + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("You want to exit the program")
        break  # and Exit the program
