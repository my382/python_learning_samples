"""Module for memory database """
import sqlite3

class MemDB:
    """Memory Database class"""
    mem_db_instance: object = None
    mem_con: sqlite3.Connection = sqlite3.connect(':memory:')

    def __new__(cls) -> object:
        """ Mem DB class single instance  """
        return_mem_db_obj: object
        if cls.mem_db_instance is None:
            cls.mem_db_instance = super().__new__(cls)

        return_mem_db_obj = cls.mem_db_instance # type: ignore
        return return_mem_db_obj

    def display(self)-> None:
        """Display"""
        print("Memory DB")