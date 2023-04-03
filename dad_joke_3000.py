from colorama import init
from termcolor import colored
from pyfiglet import figlet_format
from random import choice
import requests

init()
text = colored(figlet_format("Dad Joke 3000!"), color="cyan")
print(text)

url = "https://icanhazdadjoke.com/search"

user_input = input("Let me tell you a joke! Give me a topic: ")
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
if num_jokes > 1:
    print(f"I've got {num_jokes} jokes about {user_input}. Here's one:")
elif num_jokes == 1:
    print(f"I've got 1 joke about {user_input}. Here's one:")
else:
    print(f"Sorry, I don't have any jokes about {user_input}. Please try again.")

print(choice(res["results"])["joke"])
