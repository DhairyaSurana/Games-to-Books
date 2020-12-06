from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PATH: str = 'C:/Users/Peter/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/selenium/chromedriver.exe' # change path as needed
KEYWORDS: Dict[str, List[str]] = {"role-playing": ["fantasy", "science fiction"],  # needs more keywords added 
                                  "shooter": ["action", "war"], 
                                  "adventure": ["adventure"],
                                  "life simulation game": ["finance", "fiction"],
                                  "sandbox": ["survival", "adventure"],
                                  "war": ["war"],
                                  "strategy": ["strategy", "war", "history"],
                                  "tactic": ["strategy", "war", "history"],
                                  "tactical": ["strategy", "war", "history"],
                                  "survival": ["survival", "adventure"]
                                 }


def main() -> None:
    genres: List[str] = to_game_genre("dark souls 3")
    book_genres: List[str] = game_genre_to_book_genre(genres)
    books: List[Dict[str, str]] = []
    for item in book_genres:
        books.append(to_book(item))
    for item in books:
        print(item)


def to_game_genre(game: str) -> List[str]:
    """Takes a game and determines a list of genres which apply to it."""
    result: List[str] = []
    game.replace(" ", "+")
    URL: str = "https://www.google.com/search?q=" + game + "+game+genre"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = PATH, options = options)
    driver.get(URL)
    search = driver.find_elements_by_xpath("//*[@class = 'Z0LcW XcVN5d']")
    if len(search) < 1:
        search = driver.find_elements_by_xpath("//*[@class = 'junCMe']")
        if len(search) < 1:
            print("Error, could not find game genre.")
            return result
    for element in search:
        result.append(element.text)
    driver.close()
    return result


def game_genre_to_book_genre(input: List[str]) -> List[str]:
    """Converts a list of game genres to a list of book genres."""
    result: List[str] = []
    for string in input:
        string = string.lower()
        substrings: List[str] = string.split()
        for word in substrings:
            if word in KEYWORDS:
                for element in KEYWORDS[word]:
                    result.append(element)
        if string in KEYWORDS:
            for element in KEYWORDS[string]:
                result.append(element)
    return result


def to_book(genre: str) -> Dict[str, str]:
    """Takes a book genre and returns a dictionary of related book titles and authors."""
    genre.replace(" ", "+")
    URL: str = "https://www.google.com/search?q=best+" + genre + "+books"
    authors: List[str] = []
    books: List[str] = []
    result: Dict[str, str] = {}
    base: int = 0
    curr: int = 0
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = PATH, options = options)
    driver.get(URL)
    search1 = driver.find_elements_by_class_name("cp7THd")
    search2 = driver.find_elements_by_class_name("FozYP")
    if len(search2) == 0:
        print("Error: desired genre has no results on Google.")
        return result
    for element in search1:
        authors.append(element.text)
    for i in range(0, len(search2)):
        if search2[i].text in authors:
            curr = i
            name: str = ""
            for k in range(base, curr):
                name = name + " " + search2[k].text
            books.append(name)
            base = curr + 1
        else:
            continue
    driver.close()
    if len(authors) != len(books):
        print("Error combining book titles.")
        return result
    for j in range(0, len(authors)):
        result[books[j]] = authors[j]
    return result


#Idiom
if __name__ == "__main__":
    main()
else:
    print(__name__)