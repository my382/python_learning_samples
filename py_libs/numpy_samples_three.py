"""Array from numpy library samples"""""

import numpy as np
from numpy import ndarray


class NumpyUse:
    """NumpyUse class is used to demonstrate the use of numpy library"""
    name: str = ""

    def __init__(self) -> None:
        """Constructor of NumpyUse class"""
        self.name = "NumpyUse"

    def print_name(self) -> None:
        """Prints the name of the class"""
        print("Name is : ", self.name)

    def save_array_to_file(self, file_name: str) -> None:  # type: ignore
        """Save array to file"""
        print("Saving array to file : ", file_name)
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        np.save(file_name, arr)
        print("Array saved successfully")

    def load_array_from_file(self, file_name: str) -> None:  # type: ignore
        """Load array from file"""
        print("Loading array from file : ", file_name)
        arr = np.load(file_name)
        print("Array from file : ", arr)
        print("Array loaded successfully. ")

    def print_array_from_existing_array(self,
                                        arr: ndarray[int]) -> None:  # type: ignore
        """print array from existing array"""
        print("Existing array : ", arr)  # type: ignore
        print("New array : ", arr[3:8])  # type: ignore

    def save_array_to_csv_format(self,
                                 csv_arr: ndarray[int]) -> None:  # type: ignore
        """Save array to csv format"""
        print("Saving array to csv format : ", csv_arr)  # type: ignore
        np.savetxt('C:\\Data\\arr_file.csv', csv_arr)  # type: ignore
        print("Array saved successfully")

    def load_array_from_csv_format(self,
                                   file_name: str) -> None:  # type: ignore
        """Load array from csv file. """
        print("Loading array from csv file : ", file_name)
        arr = np.loadtxt(file_name)
        print("Array from file : ", arr)
        print("Array loaded successfully. ")


if __name__ == '__main__':
    numpy_use_instance = NumpyUse()
    numpy_use_instance.print_name()

    numpy_use_instance.save_array_to_file('C:\\Data\\arr_file.npy')
    numpy_use_instance.load_array_from_file('C:\\Data\\arr_file.npy')

    numpy_use_instance.print_array_from_existing_array(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    numpy_use_instance.save_array_to_csv_format(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    numpy_use_instance.load_array_from_csv_format('C:\\Data\\arr_file.csv')
