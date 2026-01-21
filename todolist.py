task = []

while True:
    userWish = int(input("Select what you want to do (1. add task, 2. del task, 3. view task, 4. exit): "))

    if userWish == 1:
        userInput = input("Please enter a task: ")  
        task.append(userInput)  
        print("Your task added to the list")

    elif userWish == 2:
        for index, tasklist in enumerate(task):
            print(f"{index}. {tasklist}")  
        userdelChose = int(input("Please enter the index number to delete the task: "))
        if 0 <= userdelChose < len(task):
            task.pop(userdelChose)
            print("Task deleted successfully")
        else:
            print("Invalid index! Something went wrong.")

    elif userWish == 3:
        if not task:
            print("No tasks available")
        else:
            for tasklist in task:
                print(tasklist)

    elif userWish == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Please select a valid option!")
