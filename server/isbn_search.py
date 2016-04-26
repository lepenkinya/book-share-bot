import requests
from bs4 import BeautifulSoup


class Book:
    def __init__(self, title, author):
        self.author = author.strip()
        self.title = title.strip()

    def to_string(self):
        return self.author + ', ' + self.title


def find_book_by_isbn(isbn):
    url = 'http://bookradar.org/search'
    response = requests.post(url, params={'type': 'all', 'q': isbn})
    soup = BeautifulSoup(response.content, 'html5lib')

    books = []
    for e in soup.find_all('div', {'class': "b-result"}):
        title = e.find('div', {'class': 'b-result__name-wrap'}).get_text()
        author = e.find('div', {'class': 'b-result__author'}).get_text()
        books.append(Book(title, author))

    return books

