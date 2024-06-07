#/!bin/usr/python3

import requests
import sys

if __name__ == "__name__":
    Id = sys.argv[1]
    user= f"https://jsonplaceholder.typicode.com/user/{Id}"
    todo = f"https://jsonplaceholder.typicode.com/todo"
    USER_ID = requests.get(user).json()
    
    
    
