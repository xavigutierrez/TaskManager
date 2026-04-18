from task_manager import TaskManager

def print_menu():
    print("\n---------- Task Manager ----------")
    print("\t\t1.- Add task")
    print("\t\t2.- List tasks")
    print("\t\t3.- Complete task")
    print("\t\t4.- Delete task")
    print("\t\t5.- Exit")


def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:

            choice = int(input("Choose an option: "))

            match choice:
                case 1:
                    description = input("Please provide the description for the task: ")
                    manager.add_task(description)
                    
                case 2:
                    manager.list_tasks()

                case 3:
                    id = int(input("Please provide the ID of the task to complete: "))
                    manager.complete_task(id)

                case 4:
                    id = int(input("Please provide the ID of the task to delete: "))
                    manager.delete_task(id)

                case 5:
                    print("Exiting Task Manager!")
                    break
                case _:
                    print("Invalid option. Choose again.")
        except ValueError:
            print("Invalid option. Choose again.")

if __name__ == "__main__":
    main()