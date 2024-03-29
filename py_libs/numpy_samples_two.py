"""Numpy library samples"""

import numpy as np
from numpy import ndarray


class NumpyUse:
    """NumpyUse class is used to demonstrate the use of numpy library"""
    name: str = ""

    def __init__(self) -> None:
        """Initialize the class"""
        self.name = "NumpyUse"

    def print_name(self) -> None:
        """Print the name of the class"""
        print("Name is : ", self.name)

    def print_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array"""
        print("Array is : ", arr.tolist())

    # type: ignore
    def print_vertically_stacked_array(self,
                                       arr1: ndarray[int],  # type: ignore
                                       arr2: ndarray[int]) -> None:  # type: ignore
        """Print the vertically stacked array"""
        print("Array 1 is : ", arr1.tolist())
        print("Array 2 is : ", arr2.tolist())
        print("Vertically stacked array is : ",
              np.vstack((arr1, arr2)))  # type: ignore

    # type: ignore
    def print_horizontally_stacked_array(self,
                                         arr1: ndarray[int],  # type: ignore
                                         arr2: ndarray[int]) -> None:  # type: ignore
        """Print the horizontally stacked array"""
        print("Array 1 is : ", arr1.tolist())
        print("Array 2 is : ", arr2.tolist())
        print("Horizontally stacked array is : ",
              np.hstack((arr1, arr2)))  # type: ignore

    # type: ignore
    def print_horizontal_split_array(self,
                                     arr: ndarray[int]) -> None:  # type: ignore
        """Print the horizontal split array"""
        print("Array is : ", arr.tolist())
        print("Horizontal split array is : ",
              np.hsplit(arr, 3))  # type: ignore
        print("Horizontal split array is : ",
              np.hsplit(arr, (3, 4)))  # type: ignore

    def print_array_copy(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array copy"""
        print("Array is : ", arr.tolist())
        arr1 = np.copy(arr)  # type: ignore
        print("Array copy is : ", arr1)  # type: ignore

    # type: ignore
    def print_array_addition(self,
                             arr1: ndarray[int],  # type: ignore
                             arr2: ndarray[int]) -> None:  # type: ignore
        """Print the array addition"""
        print("Array 1 is : ", arr1.tolist())
        print("Array 2 is : ", arr2.tolist())
        print("Array addition is : ", arr1 + arr2)  # type: ignore

    # type: ignore
    def print_array_subtraction(self,
                                arr1: ndarray[int],  # type: ignore
                                arr2: ndarray[int]) -> None:  # type: ignore
        """Print the array subtraction"""
        print("Array 1 is : ", arr1.tolist())
        print("Array 2 is : ", arr2.tolist())
        print("Array subtraction is : ", arr1 - arr2)

    # type: ignore
    def print_array_multiplication(self,
                                   arr1: ndarray[int],  # type: ignore
                                   arr2: ndarray[int]) -> None:  # type: ignore
        """Print the array multiplication"""
        print("Array 1 is : ", arr1.tolist())
        print("Array 2 is : ", arr2.tolist())
        print("Array multiplication is : ", arr1 * arr2)  # type: ignore

    # type: ignore
    def print_array_division(self,
                             arr1: ndarray[int],  # type: ignore
                             arr2: ndarray[int]) -> None:  # type: ignore
        """Print the array division"""
        print("Array 1 is : ", arr1.tolist())
        print("Array 2 is : ", arr2.tolist())
        print("Array division is : ", arr1 / arr2)  # type: ignore

    def print_array_sum(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array sum"""
        print("Array is : ", arr.tolist())
        print("Array sum is : ", arr.sum())

    # type: ignore
    def print_array_sum_over_axis(self,
                                  arr: ndarray[int]) -> None:  # type: ignore
        """Print the array sum over axis"""
        print("Array is : ", arr.tolist())
        print("Array sum over axis 0 is : ", arr.sum(axis=0))
        print("Array sum over axis 1 is : ", arr.sum(axis=1))

    # type: ignore
    def print_array_broadcasting(self,
                                 arr: ndarray[int],  # type: ignore
                                 multplier: int) -> None:
        """Print the array broadcasting"""
        print("Array is : ", arr.tolist())
        print("Multiplier is : ", multplier)
        print("Array broadcasting is : ", arr * multplier)

    def print_array_max(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array max"""
        print("Array is : ", arr.tolist())
        print("Array max is : ", arr.max())  # type: ignore

    def print_array_min(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array min"""
        print("Array is : ", arr.tolist())
        print("Array min is : ", arr.min())  # type: ignore

    def print_array_random(self) -> None:  # type: ignore
        """Print the array random"""
        print("Array random is : ", np.random.random((2, 3)))  # type: ignore

    def print_array_random_second(self) -> None:  # type: ignore
        """Print the array random second"""
        rng = np.random.default_rng()  # type: ignore
        arr = rng.integers(5, size=(2, 4))  # type: ignore
        print("Array random second is : ", arr)  # type: ignore

    def print_2D_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the 2D array"""
        print("2D Array is : ", arr.tolist())

    def print_unique_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the unique array"""
        print("Array is : ", arr.tolist())
        print("Unique values are : ", np.unique(arr))  # type: ignore

    # type: ignore
    def print_unique_array_with_counts(self,
                                       arr: ndarray[int]) -> None:  # type: ignore
        """Print the unique array with counts"""
        print("Array is : ", arr.tolist())
        unique_values, occurrence_counts = np.unique(arr, return_counts=True)
        print("Unique array with count are : ", unique_values,
              "occurrence count : ", occurrence_counts)  # type: ignore

    # type: ignore
    def print_unique_array_rows(self,
                                arr: ndarray[int]) -> None:  # type: ignore
        """Print the unique array rows"""
        print("Array is : ", arr.tolist())
        print("Unique rows are : ", np.unique(arr, axis=0))  # type: ignore

    # type: ignore
    def print_unique_array_columns(self,
                                   arr: ndarray[int]) -> None:  # type: ignore
        """Print the unique array columns"""
        print("Array is : ", arr.tolist())
        print("Unique columns are : ", np.unique(arr, axis=1))  # type: ignore

    # type: ignore
    def print_unique_rows_indices_occurence_count(self,
                                                  arr: ndarray[int]) -> None:  # type: ignore
        """Print the unique rows indices occurence count"""
        print("Array is : ", arr.tolist())
        unique_rows, indices, counts = np.unique(arr, axis=0,  # type: ignore
                                                 return_counts=True, return_index=True)
        print("Unique rows are : ", unique_rows)  # type: ignore
        print("Unique rows indices are : ", indices)
        print("Unique rows occurence count are : ", counts)  # type: ignore

    def print_array_reshape(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array reshape"""
        print("Array is : ", arr.tolist())
        print("Array reshape(2,3) is : ", arr.reshape(2, 3))  # type: ignore
        print("Array reshape(3,2) is : ", arr.reshape(3, 2))  # type: ignore

    def print_array_transpose(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array transpose"""
        print("Array is : ", arr.tolist())
        print("Array transpose is : ", arr.transpose())  # type: ignore

    def print_array_reverse(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array reverse"""
        print("Array is : ", arr.tolist())
        print("Array reverse using arr[::-1] is : ", arr[::-1])  # type: ignore
        reverse_arr = np.flip(arr)  # type: ignore
        print("Array reverse using np.flip(arr) is : ",
              reverse_arr)  # type: ignore

    # type: ignore
    def print_array_reverse_rows(self,
                                 arr: ndarray[int]) -> None:  # type: ignore
        """Print the array reverse rows"""
        print("Array is : ", arr.tolist())
        print("Array reverse rows is : ", np.flip(arr, axis=0))  # type: ignore

    # type: ignore
    def print_array_reverse_columns(self,
                                    arr: ndarray[int]) -> None:  # type: ignore
        """Print the array reverse columns"""
        print("Array is : ", arr.tolist())
        print("Array reverse columns is : ",
              np.flip(arr, axis=1))  # type: ignore

    def print_array_flatten(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array flatten"""
        print("Array is : ", arr.tolist())
        print("Array flatten is : ", arr.flatten())  # type: ignore

    def print_array_ravel(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print the array ravel"""
        print("Array is : ", arr.tolist())
        arr2 = arr.ravel()  # type: ignore
        print("Array ravel is : ", arr2)  # type: ignore
        arr2[0] = 98
        print("Parent Array after ravel and changed value : ", arr.tolist())
        print("Array ravel after changed value : ", arr2.tolist())

    def print_help_func(self, func_name: str) -> None:
        """Print the help function"""
        print("Help for ", func_name)
        print(help(func_name))


if __name__ == '__main__':
    print("NumpyUse class is used to demonstrate the use of numpy library")
    print("Array from numpy library samples")

    numpy_use_instance = NumpyUse()
    numpy_use_instance.print_name()

    numpy_use_instance.print_array(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # type: ignore
    numpy_use_instance.print_vertically_stacked_array(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]),  # type: ignore
                                                      np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]))
    numpy_use_instance.print_horizontally_stacked_array(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]),  # type: ignore
                                                        np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]))

    numpy_use_instance.print_horizontal_split_array(  # type: ignore
        np.arange(1, 25).reshape(2, 12))  # type: ignore
    numpy_use_instance.print_array_copy(  # type: ignore
        np.arange(1, 25).reshape(2, 12))  # type: ignore

    numpy_use_instance.print_array_addition(  # type: ignore
        np.array([1, 2]), np.ones(2, dtype=int))  # type: ignore
    numpy_use_instance.print_array_subtraction(  # type: ignore
        np.array([1, 2]), np.ones(2, dtype=int))  # type: ignore
    numpy_use_instance.print_array_multiplication(  # type: ignore
        np.array([1, 2]), np.ones(2, dtype=int))  # type: ignore
    numpy_use_instance.print_array_division(  # type: ignore
        np.array([1, 2]), np.ones(2, dtype=int))  # type: ignore

    numpy_use_instance.print_array_sum(  # type: ignore
        np.arange(1, 25).reshape(2, 12))  # type: ignore
    numpy_use_instance.print_array_sum_over_axis(  # type: ignore
        np.array([[1, 1], [2, 2]]))  # type: ignore
    numpy_use_instance.print_array_broadcasting(  # type: ignore
        np.array([1, 2]), 2)  # type: ignore
    numpy_use_instance.print_array_max(  # type: ignore
        np.arange(1, 25).reshape(2, 12))  # type: ignore
    numpy_use_instance.print_array_min(  # type: ignore
        np.arange(1, 25).reshape(2, 12))  # type: ignore
    numpy_use_instance.print_array_random()  # type: ignore
    numpy_use_instance.print_array_random_second()  # type: ignore

    numpy_use_instance.print_2D_array(  # type: ignore
        np.array([[1, 2], [3, 4], [5, 6]]))  # type: ignore
    numpy_use_instance.print_unique_array(np.array(  # type: ignore
        [[1, 1, 2, 2, 3], [6, 7, 8, 9, 10], [1, 2, 8, 9, 10]]))  # type: ignore
    numpy_use_instance.print_unique_array_with_counts(np.array(  # type: ignore
        [[1, 1, 2, 2, 3], [6, 7, 8, 9, 10], [1, 2, 8, 9, 10]]))  # type: ignore
    numpy_use_instance.print_unique_array_rows(  # type: ignore
        np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]))  # type: ignore
    numpy_use_instance.print_unique_array_columns(np.array([[1, 2, 3, 4, 5], [  # type: ignore
                                                  6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [1, 2, 3, 4, 5]]))  # type: ignore
    numpy_use_instance.print_unique_rows_indices_occurence_count(np.array(  # type: ignore
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [1, 2, 3, 4, 5]]))  # type: ignore

    numpy_use_instance.print_array_reshape(np.arange(1, 7))  # type: ignore
    numpy_use_instance.print_array_transpose(  # type: ignore
        np.array([[0, 1, 2], [3, 4, 5]]))  # type: ignore
    numpy_use_instance.print_array_reverse(np.arange(1, 7))  # type: ignore
    numpy_use_instance.print_array_reverse_rows(  # type: ignore
        np.arange(1, 7).reshape(2, 3))  # type: ignore
    numpy_use_instance.print_array_reverse_columns(  # type: ignore
        np.arange(1, 7).reshape(2, 3))  # type: ignore

    numpy_use_instance.print_array_flatten(np.array(  # type: ignore
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))  # type: ignore
    numpy_use_instance.print_array_ravel(np.array(  # type: ignore
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))  # type: ignore

    numpy_use_instance.print_help_func("max")
