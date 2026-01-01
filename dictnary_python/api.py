import requests

data = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=data)

for i,j in response.json().items():
    print(i,j)

for i,j in response.json().items():
    if i == "completed":
        if j == False:
            print("all works okay")
    if i == "userId":
        if j in [1,2,3,4]:
            print("user found")