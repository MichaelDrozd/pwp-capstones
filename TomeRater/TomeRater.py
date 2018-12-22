import re

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated to " + str(isbn))

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        average = 0
        for rating in self.ratings:
            average += rating
        average = average / len(self.ratings)
        return average

class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user’s email has been updated to " + str(address))

    def __repr__(self):
        return "User" + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        for key, value in self.books.items():
            if value != None:
                average += value
        average = average / len(self.books)
        return average

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + str(email) + "!")

    # Email validation test
    def validate_email(self, email):
        if len(email) > 7:
            return bool(re.match(
                "^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))

    def add_user(self, name, email, user_books = None):
        if self.validate_email(email) != True:
            print("Email " + email + " is invalid. Please correct your email address")
            return
        # Test if someone tries to add a user with an email that already exists
        if email in self.users:
            print(str(email) + " user already exists")
            return
        NewUser = User(name, email)
        self.users[email] = NewUser
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for key, value in self.books.items():
            print(key)

    def print_users(self):
        for key, value in self.users.items():
            print(value)

    def get_most_read_book(self):
        most_read = None
        most_read_value = 0
        for key, value in self.books.items():
            if value > most_read_value:
                most_read = key
                most_read_value = value
        return most_read

    def highest_rated_book(self):
        highest_average_rating = 0
        highest_book = None
        for key, value in self.books.items():
            if key.get_average_rating() > highest_average_rating:
                highest_book = key
                highest_average_rating = value
        return highest_book

    def most_positive_user(self):
        user_highest_average_rating = 0
        highest_rating = None
        for key, value in self.users.items():
            if value.get_average_rating() > user_highest_average_rating:
                highest_rating = value
                user_highest_average_rating = value.get_average_rating()
        return highest_rating