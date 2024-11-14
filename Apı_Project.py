import requests
import termcolor
import pyfiglet
from random import choice
header= pyfiglet.figlet_format("JOKER 4200")
header= termcolor.colored(header,color="cyan")
print(header)
term = input("Give me a topic for a joke: ")
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()
results = response_json["results"]
total_jokes = response_json["total_jokes"]
if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        choice(results)['joke']
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        results[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")