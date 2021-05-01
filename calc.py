import sys
import math
class MyExpressionParser(object):
    
    def __init__(self):
        # Cache the results for faster execution
        self.pre_calculated = {}
    def calc(self, input_string):
        # Start evaluating the nested expressions from left to right
        # create new input string with evaluted result
        while ')' in input_string:
            if input_string in self.pre_calculated:
                return self.pre_calculated[input_string]
            right_bracket = input_string.index(')')
            left_bracket = input_string[:right_bracket].rindex('(')
            partial_result = self.evaluate_simple_expression(input_string[left_bracket + 1:right_bracket])
            if left_bracket == 0:
                return partial_result
            else:
                # Reconstruct the input string to evaluate further
                input_string = input_string[:left_bracket] + str(partial_result) + input_string[right_bracket+1:]
        return int(input_string)

    # Evaluates simple expression with no nested expressions
    def evaluate_simple_expression(self, simple_expression):
        # Check if result is already calculated
        # pull from the cache if exists
        if simple_expression in self.pre_calculated:
            return self.pre_calculated[simple_expression]
        pieces = simple_expression.split()
        operator = pieces[0]
        args = [int(p) for p in pieces[1:]]
        # We can conditions for more operators below
        if operator == 'add':
            answer =  sum(args)
        elif operator == 'multiply':
            answer = math.prod(args, start=1)
        elif operator == 'exponent':
            answer = args[0]**args[1]
        else:
            answer = int(simple_expression)
        # Add to cache
        self.pre_calculated[simple_expression] = answer
        return answer

if __name__ == '__main__':
    parser = MyExpressionParser()
    inputs = sys.argv[1]
    result = parser.calc(inputs)
    print(result)