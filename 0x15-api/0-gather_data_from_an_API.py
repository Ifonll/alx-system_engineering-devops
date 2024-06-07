#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    User= f"https://jsonplaceholder.typicode.com/users/{ID}"
    Todos = f"https://jsonplaceholder.typicode.com/todos"
    
    employee = requests.get(User).json()
    tasks = requests.get(Todos, params={"userId" : ID}).json()
    name = employee.get("name")
    completed = []
    for task in tasks:
        if (task.get("completed")):
            title = task.get("title")
            completed.append(title)

    output = f"Employee {name} is done with tasks({len(completed)}/{len(tasks)}):"
    print(output)
    
    for task in completed:
        print("\t " + task)
        
    print(employee)