def check_sequence(string1, string2):
    index = -1
    for char in string2:
        index = string1.find(char, index + 1)
        if index == -1:
            return False
    return True


def read_input():
    return input(), input()


if __name__ == '__main__':
    string2, string1 = read_input()
    print(check_sequence(string1, string2))
