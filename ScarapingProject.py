# scrapy framework
import requests
from bs4 import BeautifulSoup
from random import choice

Base_url = "https://quotes.toscrape.com/"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{Base_url}{url}")
        print(f"Now Scraping: {Base_url}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "Text": quote.find(class_="text").get_text(),
                "Author": quote.find(class_="author").get_text(),
                "Link": quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

    return all_quotes


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here is a quote:")
    print(quote["Text"])
    guess = ''

    while guess.lower() != quote["Author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Remaining guesses: {remaining_guesses}\n")
        if guess.lower() == quote["Author"].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{Base_url}{quote['Link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            born_date = soup.find(class_="author-born-date").get_text()
            born_location = soup.find(class_="author-born-location").get_text()
            print(f"Hint: The author was born on {born_date} {born_location}.")
        elif remaining_guesses == 2:
            print(f"Hint: The author's first name starts with {quote['Author'][0]}.")
        elif remaining_guesses == 1:
            last_name_starts = quote["Author"].split(" ")[1][0]
            print(f"Hint: The author's last name starts with {last_name_starts}.")
        else:
            print(f"You ran out of guesses :( The answer was {quote['Author']}.")


def play_game():
    quotes = scrape_quotes()
    while True:
        start_game(quotes)
        again = input("Do you want to play again? (y/n): ").lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


play_game()
