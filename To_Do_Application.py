tasks = []

print("Welcome to the To-Do Application!")

while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    
    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    del tasks[num-1]
                    print("Task deleted!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1-4.")
