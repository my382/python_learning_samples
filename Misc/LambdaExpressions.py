
# Lambda Expressions in python

class LambdaExpressions: 

    # Returns an incrementor for the given number
    def make_incrementor(self, num):
        return lambda x: x + num

    # Returns a sorted list for the given sort key. 
    def sort_list_using_lambda_expression(self, list, sort_key): 
        return sorted(list, key=sort_key)
    
leObj = LambdaExpressions()
incrementor = leObj.make_incrementor(10)
print("Make incrementor for 10 using lambda expressions : ", incrementor(0), incrementor(1))

pairs = [(1, 'one'), (3,'three'), (5,'five'), (2,'two'), (4, 'four')]
sorted_pairs =  leObj.sort_list_using_lambda_expression(pairs, lambda pair: pair[0])
print("pairs before sorting: ", pairs)
print("pairs after sorting: ", sorted_pairs)
