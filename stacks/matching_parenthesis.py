""" Matching the parenthesis from string using stack """


def is_balanced(string_input: str) -> bool:
    left_paranthesis = []
    lookup_table = {'(': ')', '[': ']', '{': '}'}

    for character in string_input:
        if character in lookup_table:
            left_paranthesis.append(character)
        elif not left_paranthesis or lookup_table[left_paranthesis.pop()] != character:
            return False
    
    return not left_paranthesis


print(is_balanced("[()]("))
