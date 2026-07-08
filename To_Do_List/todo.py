import os
def load_tasks():
    if not os.path.exists("todo.txt"):
        return[]
    with open("todo.txt","r") as f:
        #Read lines and strip newline characters
        return[line.strip() for line in f.readlines()]
    #update main to use this
    #def main()
    #tasks = load_tasks()
    
def save_tasks(tasks):
    with open("todo.txt","w") as f:
        for task in tasks:
         f.write(task + "\n")      

def main():
    tasks = []
    while True:
        print("\n---To-Do List App---")
        print("01.View Tasks")
        print("02.Add Task")
        print("03.Remove Task")
        print("04.Exit")

        choice =input("Enter your choice (1-4): ")
        if choice == '1':
            print("\n Your Tasks:")
            if not tasks:
                print("Your To Do List is empty")
            else:
                for index,task in enumerate(tasks, start=1):
                    print(f"{index}.{task}")   
            pass 
        elif choice == '2':
            task = input("Enter the task:")
            tasks.append(task)
            print("Task added!")

        elif choice == '3':
            #Show task first
            for index, task in enumerate(tasks,start=1):
                print(f"{index}.{task}")

                try:
                    task_num = int(input("Enter task number to remove:"))
                    if 0 < task_num <= len(tasks):
                        removed = tasks.pop(task_num -1)
                        save_tasks(tasks)
                        print(f"Removed:{removed}")
                    else:
                        print("Invlid task number.")
                except ValueError:
                  print("Please enter a valid number.")                        
            pass    
        #call this function whenever we add or remove a task
        #save_tasks(tasks)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice,please try again.")

if __name__ == "__main__":
   main()
