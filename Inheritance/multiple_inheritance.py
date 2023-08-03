
# Base Class 1 added with members and display method. 
class BaseClass1: 
    int_base1_member : int = 1
    str_base1_member : str = "Base Class One"

    def display_base1(self): 
        return self.str_base1_member

# Base Class 2 added with members and display method. 
class BaseClass2: 
    int_base2_member : int = 2
    str_base2_member : str = "Base Class Two"

    def display_base2(self): 
        return self.str_base2_member


# Derived Class inherited from base class and added its members & display method. 
class DerivedClass(BaseClass1, BaseClass2): 
    int_derived_member : int =2
    str_derived_member : str  = "Derived Class"

    def display_derived(self): 
        return self.str_derived_member



if __name__ == '__main__': 
    # Derived Class instance created. 
    derived_instance = DerivedClass()

    # Invoked Base class One method
    print("Base Class One method invocation: ",  derived_instance.display_base1())

    # Invoked Base class Two method
    print("Base Class Two method invocation: ",  derived_instance.display_base2())

    # Invoked Derived class method. 
    print("Derived Class method invocation: ",  derived_instance.display_derived())