""" Module for db operations."""
import sqlite3

class DBOperations:
    """ Database operations """

    con: sqlite3.Connection
    cur: sqlite3.Cursor
    data: sqlite3.Cursor
    is_open_connection: bool

    def open_connection(self, db_path_name: str) -> bool | None:
        """ Function opening DB connection. """
        self.is_open_connection = False
        try:
            # In memory DB connection
            # self.con = sqlite3.connect(":memory:")

            # DB file will be opened if exists or created new to establish connection
            self.con = sqlite3.connect(db_path_name)
            print("Database connection established successfully. ")
            self.is_open_connection = True

        except ConnectionError as conn_error:
            print(conn_error)
            self.is_open_connection = False

        return self.is_open_connection

    def close_connection(self) -> bool | None:
        """ Closing connection """
        is_close_connection: bool = False
        try:
            if self.is_open_connection:
                self.con.close()
                print("Database connection closed successfully. ")
                is_close_connection = True

        except ConnectionError as conn_error:
            print(conn_error)
            is_close_connection = False

        return is_close_connection

    def exec_ddl_statements(self, ddl_statement: str) -> None:
        """ Execute DDL Statements """
        try:
            if self.is_open_connection:
                self.cur = self.con.cursor()
                self.data = self.cur.execute(ddl_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)


    def exec_batch_ddl_statements(self, ddl_statement: str) -> None:
        """ Execute Batch DDL Statements """
        try:
            if self.is_open_connection:
                self.cur = self.con.cursor()
                self.data = self.cur.executescript(ddl_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

    def exec_dml_statements(self, dml_statement: str, sql_parameters = None) -> None:  # type: ignore
        """ Execcute DML Statements """
        try:
            if self.is_open_connection:
                self.cur = self.con.cursor()

            if sql_parameters is not None:
                self.data = self.cur.execute(dml_statement, sql_parameters)
            else:
                self.data = self.cur.execute(dml_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)


    def exec_batch_dml_statements(self, dml_statement: str, sql_params = None) -> None:
        """ Executing batch DML statements """
        try:
            if self.is_open_connection:
                self.cur = self.con.cursor()

            if sql_params is not None:
                self.data = self.cur.executemany(dml_statement, sql_params)
            else:
                self.data = self.cur.execute(dml_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

    def display_data(self) -> None:
        """ Displaying data received from DML statement such as SELECT. """
        try:
            print("Table Data: \n")
            if self.data.rowcount > 0:
                for row in self.data:
                    print(row)
            else:
                print(
                    "There is a problem in the connection or No records available to display. ")
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

    def display_scalar_data(self) -> None:
        """ Displaying data received from DML statement such as SELECT. """
        try:
            print("Table Data: \n")
            if self.data.rowcount > 0:
                print("Scalar Value: ", self.data.fetchone())
            else:
                print(
                    "There is a problem in the connection or No records available to display. ")
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

if __name__ == '__main__':
    db_instance = DBOperations()
    db_path: str = "C:\\Data\\Students.db"
    is_connection_success: bool | None = db_instance.open_connection(
        db_path)
    if is_connection_success:

        db_instance.exec_ddl_statements(
            'CREATE TABLE Student(StudentId, Name)')

        db_instance.exec_dml_statements(
            "INSERT INTO Student VALUES(?,?)", (1, "Scott"))
        db_instance.exec_dml_statements(
            "INSERT INTO Student VALUES(?,?)", (2, "Martin"))
        db_instance.exec_dml_statements("SELECT StudentId, Name FROM Student")
        db_instance.display_data()

        db_instance.exec_dml_statements(
            "SELECT COUNT(StudentId) as num_of_students FROM Student")
        db_instance.display_scalar_data()

        db_instance.exec_ddl_statements(
            "CREATE TABLE Marks(MarksId, StudentId, SubjectName, SubjectMarks)")
        db_instance.exec_batch_dml_statements("INSERT INTO Marks(MarksId, StudentId, SubjectName, SubjectMarks) VALUES(?,?,?,?)",
                                              [(1, 1, "Physics", 75),
                                               (2, 1, "Chemistry", 85),
                                                  (3, 1, "Maths", 90),
                                                  (4, 1, "Biology", 78)])
        db_instance.exec_dml_statements(
            "SELECT MarksId, StudentId, SubjectName, SubjectMarks FROM Marks")
        db_instance.display_data()

        db_instance.exec_batch_ddl_statements("""
                                    BEGIN;
                                    CREATE TABLE Person(PersonId, FirstName, LastName, Age);
                                    CREATE TABLE Book(BookId, Title, Author, Published);
                                    CREATE TABLE Publisher(PublisherId, Name, Address);
                                    COMMIT;
                                        """)
        db_instance.close_connection()
