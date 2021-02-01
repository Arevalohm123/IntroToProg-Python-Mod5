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
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare Variables and Constants
todo = "C:\\_PythonClass\\Assignment05\\ToDoList.txt"   # The To-Do List
New_Task = None                                         # New task
New_Priority = None                                     # Priority of new task
New_Row = (New_Task, New_Priority)                      # New task grouped with its priority
strTaskRemove = None                                    # Task that will be removed
Table = []                                              # Table of tasks and priorities put together

# -- Processing -- #
# This loop takes the to-do list file and adds it to a table
objFile = open(todo)
for row in objFile:
    T, P = row.split(",")
    newEntry = (T, P.strip())
    Table.append(newEntry)


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
        table_range = len(Table) - 1
        k = 0
        print("Task, Priority")
        print("---------------")
        while k <= table_range:
            y = str(Table[k][0])
            z = str(Table[k][1])
            print(y, ",", z)
            k = k + 1
        continue
    # Step 4 - Add a new item to the list/Table
    #   Use New_Task and New_Priority to gather inputs from the user. Take this data and
    #   append it to the imported Table, and then print a confirmation message to the user.
    elif strChoice.strip() == '2':
        New_Task = input("What's the task you'd like to add?")
        New_Priority = input("What's the priority?(1-5)")
        New_Row = (New_Task, New_Priority)
        Table.append(New_Row)
        print("\n" + New_Task + " has been added with a priority of " + New_Priority + "!")
        continue
    # Step 5 - Remove a new item from the list/Table
    #   Use StrTaskRemove to get the users input on which task to remove. Find this task in
    #   the first column of the latest version of the Table, and if it exist, delete it.
    elif strChoice.strip() == '3':
        print("Tasks available for deletion:")
        print("------------------------------")
        table_range = len(Table) - 1
        k = 0
        print("Task, Priority")
        print("---------------")
        while k <= table_range:
            y = str(Table[k][0])
            z = str(Table[k][1])
            print(y, ",", z)
            k = k + 1
        strTaskRemove = str(input("\nWhich task would you like to remove?"))
        j = 0
        while j <= table_range:
            if strTaskRemove in Table[j]:
                del Table[j]
                print("\n" + strTaskRemove + " has been successfully deleted!")
                break
            else:
                j = j + 1
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        g = 0
        table_range = len(Table) - 1
        file = open(todo, "w+")
        while g <= table_range:
            save_task = str(Table[g][0])        # Task that will be saved
            save_priority = str(Table[g][1])    # Priority of task to be saved
            file.write(save_task + "," + save_priority + "\n")
            g = g + 1
        print("\nYou're file has been saved!")
    # Step 7 - Exit program
    #   Print a message showing the script is closing and end the program.
    elif strChoice.strip() == '5':
        print("The program is now closing")
        break  # and Exit the program
