"""Module for Dictionary comprehensions """
class DictionaryComprehensions:
    """ Dictionary Comprehensions class """

    def get_dict_comprehension(self, range_val: int) -> dict[int, int]:
        """ dict comprehensions """
        # Here a number will be taken from the given range
        # it will start making its square.
        return {num: num ** 2 for num in range(range_val)}

    def formulating_dict(self, str_list: list[str] ) -> dict[int, str]:
        """dict comprehensions and formulating dict """
        new_dict: dict[int, str] = {0:''}
        index: int = 0
        for str_val in str_list:
            new_dict[index] = str_val
            index = index+1

        return new_dict


if __name__ == '__main__':
    dc_instance = DictionaryComprehensions()
    print('Dictionary comprehension for the given range: ',
          dc_instance.get_dict_comprehension(10))
    fruits: list[str] = ['Mango', 'Strawberry', 'Pear', 'Apple']
    print('List of fruits before formulating dict: ', fruits)
    print('After dictionary formulation: ', dc_instance.formulating_dict(fruits))
