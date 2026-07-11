task=[]
while True:
    choice=input("type 'add', 'view', 'remove', or 'done': ")
    if choice=="add":
        new_task=input("what you want to add: ")
        task.append(new_task)
    elif choice=="view":
        print(task)
    elif choice=="remove":
        remove_task=input("which task do you want to remove: ")
        task.remove(remove_task)
    elif choice=="done":
        break
