
"""
This simple application is a todo app that helps a user keep track of
their todo list activities.

This application is designed for every beginners in python looking for application
to built after learning the basics of Python Programming language.

Developer: Olamilekan aka intellisenseCoder.

Schema:
======================================================================================================
S/N                 TASKS                                               DATE                TIME
======================================================================================================
1.                  Start Learning Python Programming Language          27/08/2022          8:00 AM
2.                  Take my cat on a walk                               27/08/2022          6:50 PM
...
...
...

"""
import util as ut
import message as msg

print("Hello, Welcome to your TODO APP.\nKeep track of your todo activities.")


start = True

while start:
    operation = input("\n\nSelect Operation to perform: \n1. Display All Tasks \n2. Add New Task \n3. Edit Task \n4. Delete Task \n5. Quit \n\nEnter your operation: ")
    try:
        if operation == "1":
            ut.displayTodoList()

        elif operation == "2":
            # call addTask funct
            task = input("Enter your task: ")
            ut.addNewTask(task)
            msg.successMsg("SUCCESSFULLY")
        elif operation == "3":
            # call editTask funct
            ut.displayTodoList()
            try:
                taskIndex = input("Select the Task to edit (S/N): ")
                editedTask = ut.editTask(taskIndex)
                msg.successMsg("EDITTED")
            except IndexError:
                print("INVALID: There is no task present in row {}".format(taskIndex))
            except:
                print("ERROR: An error occured")
        elif operation == "4":
            # call deleteTask funct
            ut.displayTodoList()
            
            try:
                taskIndex = input("Select the Task to delete (S/N): ")
                ut.deleteTask(taskIndex)
                msg.successMsg("DELETED")
            except IndexError:
                print("INVALID: There is no task present in row {}".format(taskIndex))
            except:
                print("ERROR: An error occured")
        elif operation == "5":
            start = False
            print("You Quit! Thank you for using our App.")
            ut.displayTodoList()
        else:
            pass
    except ValueError:
        print("TRY AGAIN! You entered and invalid operation.")
    
   
