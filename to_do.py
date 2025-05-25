def todo():
    n=int(input("enter the no. of tasks to need to add to the list:"))
    print("starting list")
    tasks=[]
    for i in range(n):
        task=input(f"enter task {i+1}: ")
        tasks.append(task)
    
    print("Your to-do list:")
    for i in range(n):
        print(f"{i + 1}. {tasks[i]}")

todo()