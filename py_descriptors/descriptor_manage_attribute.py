"""Module for descriptor manage attribute """
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:
    """Logged Age Access """

    # def __init__(self) -> None:
    #     """Initializing logging """

    def __get__(self, obj: object, objtype: object | None = None)-> None | object:
        """Logging and getting person age """
        value: object = obj._age #type: ignore    # Dynamic object with managed attribute
        logging.info('Accessing %r giving %r', 'age', value) # type: ignore
        return value # type: ignore

    def __set__(self, obj: object, value: object) -> None:
        """Logging and setting persson age """
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value # type: ignore


class Person:
    """Person class """
    age: object | None = LoggedAgeAccess()  # here age is activing as a member of
                             # class Person but a managed attribute
    name: str = '' # A member of class person but a regular attribute.

    def __init__(self, person_name: str, person_age: int) -> None:
        """Initializing age and name """
        self.name = person_name
        self.age = person_age


    def birthday(self) -> None:
        """Person's birthday so increasing age by one """
        self.age = self.age + 1 #type: ignore

    def display_person_dtls(self)-> None:
        """Person's details """
        print('name: ', self.name, ' age: ', self.age)


if __name__ == '__main__':
    person_one = Person('Person one', 26)
    print('Using Manage attribute: Person name: ',
          person_one.name, ' age: ', person_one.age) #type: ignore
    person_one.birthday()
    print('After birthday call, Person name: ',
          person_one.name, ' age: ', person_one.age) #type: ignore
    person_one.display_person_dtls()
