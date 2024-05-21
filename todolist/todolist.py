l = []
def add_task(t):
    task = {"task": t,
            "Done":False
    }
    l.append(task)
    print(f"Task added. {t}")

def delete_task(index):
    if 0 <= index < len(l):
        l.remove(index)
    else:
        print("No task found.")


def task_done(index):
    if 0 <= index < len(l):
        l[index]["Done"] = True
        print(f"Task {l[index]} completed.")
    else:
        print("No task found.")

def view():
    if len(l) == 0:
        print("No tasks found.")
    else:
        for i in l:
            print(i)

def main():
    while True:
        print("1- Add task.")
        print("2- Remove task.")
        print("3- Complate task.")
        print("4- View tasks.")
        print("q- Quit.")

        x = input("Choice: ")
        
        if x == "1":
            t = input("Enter task: ")
            add_task(t)
        elif x == "2":
            index = input("Enter task number to remove: ")
            ind = index-1
            delete_task(ind)
        elif x == "3":
            index = input("Enter task number to complate.")
            ind = index-1
            task_done(ind)
        elif x == "4":
            view()
        elif x == "q":
            print("Quiting")
            break
        else:
            print("Chose a valid option.")

main()
