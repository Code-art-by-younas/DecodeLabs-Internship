task = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    user = input("Enter your choice (1-4): ")
    
    # Invalid input check (non-digit)
    if not user.isdigit():
        print("❌ Invalid input! Please enter a number.")
        continue
    
    user = int(user)
    
    # ---------- ADD ----------
    if user == 1:
        new_task = input("Enter task: ")
        task.append(new_task)
        print(f"✅ Task added: {new_task}")
    
    # ---------- VIEW ----------
    elif user == 2:
        if not task:
            print("📭 No tasks yet.")
        else:
            print("\n📋 Your Tasks:")
            for index, t in enumerate(task, start=1):
                print(f"   {index}. {t}")
    
    # ---------- DELETE ----------
    elif user == 3:
        if not task:
            print("📭 No tasks to delete.")
        else:
            # Show tasks with numbers
            print("\n📋 Your Tasks:")
            for index, t in enumerate(task, start=1):
                print(f"   {index}. {t}")
            
            # Ask which task to delete
            delete_num = input("Enter task number to delete: ")
            
            # Check if input is valid number
            if not delete_num.isdigit():
                print("❌ Invalid input! Please enter a number.")
                continue
            
            delete_num = int(delete_num)
            
            # Check if number is within range
            if 1 <= delete_num <= len(task):
                deleted_task = task.pop(delete_num - 1)  # -1 because list index starts at 0
                print(f"✅ Task deleted: {deleted_task}")
            else:
                print(f"❌ Invalid task number! Choose between 1 and {len(task)}.")
    
    # ---------- EXIT ----------
    elif user == 4:
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice! Please select 1, 2, 3, or 4.")