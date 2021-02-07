# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog:
# AArevalo, 1.23.2021,  1st iteration
# AArevalo, 1/23/2021,  Added code to continue assignment
# AArevalo, 1/26/2021,  Fixed table viewing issues and cleaned questions
# AArevalo, 1/31/2021,  Adding comments and descriptions
# AArevalo, 2/6/2021,   Big rewrite using dictionaries instead of tables
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare Variables and Constants
todo = "C:\\_PythonClass\\Assignment05\\ToDoList.txt"   # The To-Do List
New_Task = None                                         # New task
New_Priority = None                                     # Priority of new task
dicRow = {}                                             # Dictionary entry
strTaskRemove = None                                    # Task that will be removed
strChoice = None                                        # Choice in the menu
Table = []                                              # Table of tasks and priorities put together

# -- Processing -- #
# This loop takes the to-do list file and adds it to a table
objFile = open(todo)
for row in objFile:
    lstData = row.split(",")
    dicRow = {"Task": lstData[0].strip(), "Priority": lstData[1].strip()}
    Table.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user


while True:
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
    if strChoice.strip() == '1':
        print("Task - Priority")
        print("---------------")
        for row in Table:
            print(row["Task"] + " - " + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    #   Use New_Task and New_Priority to gather inputs from the user. Take this data and
    #   append it to the imported Table, and then print a confirmation message to the user.
    elif strChoice.strip() == '2':
        New_Task = input("What's the task you'd like to add?")
        New_Priority = input("What's the priority?(1-5)")
        New_Row = {"Task": New_Task, "Priority": New_Priority}
        Table.append(New_Row)
        print("\n" + New_Task + " has been added with a priority of " + New_Priority + "!")
        continue
    # Step 5 - Remove a new item from the list/Table
    #   Use StrTaskRemove to get the users input on which task to remove. Find this task in
    #   the first column of the latest version of the Table, and if it exist, delete it.
    elif strChoice.strip() == '3':
        strTaskRemove = str(input("\nWhich task would you like to remove?"))
        table_range = len(Table) - 1
        i = 0
        while i <= table_range:
            if strTaskRemove in str(list(dict(Table[i]).values())[0]):
                del Table[i]
                print("\n" + strTaskRemove + " has been successfully deleted!")
                break
            else:
                print("Task does not exist in the to-do list!")
                i = i + 1
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        save_yesno = input("Are you sure you want to save?(y/n)")
        if save_yesno == "y":
            objFile = open(todo, "w")
            for dicRow in Table:
                objFile.write(dicRow["Task"]+"," + dicRow["Priority"] + "\n")
            objFile.close()
            print("\nYou're file has been saved!")
        else:
            print("\nYou're file has not been saved!")
            continue
    # Step 7 - Exit program
    #   Print a message showing the script is closing and end the program.
    elif strChoice.strip() == '5':
        print("The program is now closing. Goodbye!")
        break  # and Exit the program
