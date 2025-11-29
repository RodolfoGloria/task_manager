from database.db import init_db, add_task, list_tasks

def main():
    print("Initializing DB...")
    init_db()

    print("Adding example tasks...")
    add_task("Learn SQL", "Practice select and joins")
    add_task("Study Python", "Make portfolio project")

    print("\nCurrent tasks:")
    for task in list_tasks():
        print(f"{task['id']}: {task['title']} - {task['description']}")

if __name__ == "__main__":
    main()
