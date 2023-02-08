def add(task_list, task):
    task_list.append(task)

def view(task_list):
    for i in range(0, len(task_list)):
        print(str(i+1) + ") " + str(task_list[i]))

def mark(task_list, task_num):
    task_num = task_num - 1
    if 0 <= task_num < len(task_list):
        task_list[task_num] += " COMPLETE!"
    else:
        print("Task does not exist!")


task_list = []

while(True):
    print("1 -> ADD || 2 -> VIEW || 3 -> MARK || 4 -> BREAK")
    print("Which action do you want to perform?")
    action = input("> ")
    try:
        action = int(action)
        if action == 1:
            task = input("Write your task > ")
            add(task_list, task)
        elif action == 2:
            view(task_list)
        elif action == 3:
            task_num = input("Write a task number > ")
            task_num = int(task_num)
            mark(task_list, task_num)
        elif action == 4:
            break
        else:
            print("You type a wrong action, try again!")
        print()
    except Exception as e:
        print(e)
        print("You type a wrong input, try again!")