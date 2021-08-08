""" THis file implements RPN (reverse polish notation) using stack """


def evaluate_expression(expression):
    DELIMITER = ','
    INTERMEDIATE_RESULTS = []
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x / y
    }

    for each_value in expression.split(DELIMITER):
        if each_value in OPERATORS:
            # pops out the last two values from the list and perform operations on it and again append it to list.
            INTERMEDIATE_RESULTS.append(OPERATORS[each_value](INTERMEDIATE_RESULTS.pop(), INTERMEDIATE_RESULTS.pop()))
        else:
            # if it is just the number, adds to the end of the list.
            INTERMEDIATE_RESULTS.append(int(each_value))

    return INTERMEDIATE_RESULTS[-1]


evaluate_expression("3,4,+,2,*,1,+")
