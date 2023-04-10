import requests  # The requests module allows you to send HTTP requests using Python.

class MyUser:
    def __init__(self, id, email, username, name):
        self.id = id
        self.email = email
        self.username = username
        self.name = name

    def __str__(self):
        return f"User ID: {self.id}, Name: {self.name}, Email: {self.email}, Username: {self.username}"

url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url)

if res.status_code == 200: # Success request
    users_info = res.json()
    name = input("Enter a user name: ")
    found_user = False
    for user in users_info: # check for a match between the user input to user_info
        if user["name"] == name:
            found_user = True
            u = MyUser(user["id"], user["email"], user["username"], user["name"])  # Print the user details
            print(u)
            break
    if not found_user:
        print("User not found.")
else:
    print(f"Error: {res.status_code}") # Failed  request
