def check_combo(input_: int, prefix='') -> str:
    COMBO = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')
    }
    result = []

    def arrange(number, prefix):
        if number == '':
            result.append(prefix)
        else:
            for char in COMBO[number[0]]:
                arrange(str(number)[1:], prefix + char)

    arrange(str(input_), '')
    return ' '.join(result)


if __name__ == '__main__':
    print(check_combo(int(input())))
