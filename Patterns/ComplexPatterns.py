# Complex Patterns and a wildcard 


from enum import Enum


class Point: 
    x: int
    y: int

    def __init__(self, x, y):
        self.x =  x
        self.y = y

class Color(Enum): 
    RED = 0, 
    GREEN = 1, 
    BLUE = 2    

class ComplexPatterns: 

    def complex_pattern_sample(self, test_variable): 

        match test_variable: 
            case ('warning', code, 40): print(' A warning has been received.')
            case (x, y as int, *rest) : print(' Sequence pattern supports wildcards. ')
            case ('error', code, _): 
                print(f"An error {code} occurred.")

    def complex_pattern_with_guard(self, point):
        
        match point: 
            case Point(x=x,y=y) if x==y: print(f"The point is located at diagonal Y=X at {x}") 
            case Point(x=x,y=y): print(f"Point is not on the diagonal. ")
            # case (Point(x=x,y=y), Point(x=x,y=y) as p2): print(" Subpattern capturing using as. ") # Subpattern gives an error

    def enumeration_pattern(self, color): 
        
        match color: 
            case Color.RED : print('Print Red')
            case Color.GREEN: print('Print Green')
            case Color.BLUE: print('Print Blue')


cpInstance = ComplexPatterns()
cpInstance.complex_pattern_sample((5,5,'_')) 
cpInstance.complex_pattern_sample(('error','code',800)) 
cpInstance.complex_pattern_with_guard(Point(5,7))
# cpInstance.complex_pattern_with_guard( Point(5,7), Point(10,10) as p2 ) Getting syntax error when placing a call [SyntaxError: multiple assignments to name 'x' in pattern.]
cpInstance.enumeration_pattern(Color.BLUE)