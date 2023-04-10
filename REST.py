import requests # The requests module allows you to send HTTP requests using Python.
import time # The time module enables working with time in Pytho

class Rest:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f"Full Name:  {self.first} {self.last}"

while True:
    try:
        number_by_user = int(input("Please Enter a Number in the range of 0 - 100: "))
        if number_by_user > 100:
            print('Not in range')
        else:
            break
    except:
        print('Invalid input. Please enter a valid Number.')

print(f'Processing {number_by_user} API requests...')
time.sleep(3)

for number in range (number_by_user):
    url = "https://randomuser.me/api/"
    res = requests.get(url)

    users_info = res.json()
    first_name = users_info["results"][0]["name"]["first"]
    last_name = users_info["results"][0]["name"]["last"]
    u = Rest(first_name, last_name)  # create object of class with retrieved name
    print(u)


