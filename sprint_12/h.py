def is_correct_bracket_seq(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0

def read_input():
    return is_correct_bracket_seq(input())

def main():
    print(read_input())

if __name__ == '__main__':
    main()