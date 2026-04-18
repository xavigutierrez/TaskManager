from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    print("\n---------- Task Manager ----------")
    print("\t\t1.- Add task")
    print("\t\t2.- Add complex task (with AI assit)")
    print("\t\t3.- List tasks")
    print("\t\t4.- Complete task")
    print("\t\t5.- Delete task")
    print("\t\t6.- Exit")


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
                    description = input("Please provide the description for the complex task: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break
                
                case 3:
                    manager.list_tasks()

                case 4:
                    id = int(input("Please provide the ID of the task to complete: "))
                    manager.complete_task(id)

                case 5:
                    id = int(input("Please provide the ID of the task to delete: "))
                    manager.delete_task(id)

                case 6:
                    print("Exiting Task Manager!")
                    break
                case _:
                    print("Invalid option. Choose again.")
        except ValueError:
            print("Invalid option. Choose again.")

if __name__ == "__main__":
    main()