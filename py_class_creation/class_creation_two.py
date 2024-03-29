"""Module for class creation in Python """

class TestClass:
    """ Test class """
    int_member: int = 12345

    def __init__(self) -> None:
        """ Default Constructor """

    def get_int_member(self) -> int:
        """ Get int member """
        return self.int_member

    def display(self) -> str:
        """ display method of Test class """
        return 'Hello World'

if __name__ == '__main__':
    # Class Instance creation
    tc_instance = TestClass()

    print(tc_instance.int_member)
    print(tc_instance.display())
