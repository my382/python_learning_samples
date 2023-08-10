"""Module for string prefix methods """

class StringPrefixMethods:
    """String prefix methods class """

    def string_removeprefix(self, original_str: str, prefix_str: str) -> str:
        """Remove string prefix method """
        return original_str.removeprefix(prefix_str)

    def string_removesuffix(self, original_str: str, suffix_str: str) -> str:
        """Remove string suffix method """
        return original_str.removesuffix(suffix_str)

if __name__ == '__main__':
    spm_instance = StringPrefixMethods()
    original_str = "TestAdded"
    print("Original String: ", original_str, " String After Removing prefix 'Test' using removeprefix string method. ", spm_instance.string_removeprefix(original_str,"Test") )
    print("Original String: ", original_str, " String After Removing suffix 'Added' using removesuffix string method. ", spm_instance.string_removesuffix(original_str,"Added"))


