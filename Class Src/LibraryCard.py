from random import randint
import datetime as dt

class LibraryCard:

    def __init__(self, issued_date = dt.datetime.now() , expiration_date= dt.datetime.now() + dt.timedelta(weeks=100) ):
        """
        Represents data of a Library Card

        Args:
            issued_date (datetime) - library card issue date
            expiration_date (datetime) - expiration date of the library card
        """
        
        self.id = UniqueIDGenerator().id
        self.issued_date = issued_date
        self.expiration_date = expiration_date


    def __repr__(self) -> str:
        return f"LibraryCard(id={self.id}, issued_date={self.issued_date}, expiration_date={self.expiration_date})"


class UniqueIDGenerator:
    unique_ids = []

    def __init__(self):
        """
        Class to generate a unique random int
        """
        self.id = self.generate_new_id()

    def generate_new_id(UniqueIDGenerator):
        # Keep trying to generate unique ID.
        # Once found, add to the list and return
        while True:
            new_id = randint(100000000,999999999)
            if new_id not in UniqueIDGenerator.unique_ids:
                UniqueIDGenerator.unique_ids.append(new_id)
                return new_id
