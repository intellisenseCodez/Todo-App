
todoList = []
# addNew Task function
def addNewTask(task):
    """This function add a new task to
    the list of tasks"""
    todoList.append(task)
    return todoList

# deleteTask function
def deleteTask(index):
    todoList.pop(int(index)-1)
    return todoList

def editTask(index):
    todoList[int(index)-1] = input("Edit your Task: ")
    return todoList

def displayTodoList():

    print("======================================================================================================")
    print("S/N                 TASKS                                               DATE                TIME")
    print("======================================================================================================")

    if len(todoList) > 0:
        for sn in range(len(todoList)):
            print("{}                    {}                                                                        ".format(sn+1,todoList[sn]))
    else:
        print("                                            N0 TASK FOUND                                          ")
