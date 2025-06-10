class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first.lower()}. {last.lower()}@library.com'

    def fullname(self):
        return f'{self.first} {self.last}'


class Librarian(Person):
    def __init__(self, first, last, employee_id):  #instantiate the Librarian class
        super().__init__(first, last)
        self.employee_id = employee_id

    def issue_book(self, book_title):
        print(f"{self.fullname()} has issued the book: {book_title}")

class Member(Person):
    def __init__(self, first, last, membership_id):
        super().__init__(first, last)
        self.membership_id = membership_id

    def borrow_book(self, book_title):
        print(f"{self.fullname()} has borrowed the book: {book_title}")


librarian_1 = Librarian('Nick', 'Jonas', 'RJ345WQ')
member_1 = Member('Patrice', 'Roberts', 'QWERTY454')

print(librarian_1.fullname())
print(member_1.fullname())

librarian_1.issue_book('The Guest House by Rumi')
member_1.borrow_book("Oh the Places You'll Go! by Dr. Seuss")



