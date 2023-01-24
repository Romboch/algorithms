from typing import List


def get_parenthesis(n: int) -> List[str]:
    result = []
    len_prefix = n * 2
    def arrange(number: int, prefix: str) -> None:
        if number == 0:
            if prefix not in result and len(prefix) == len_prefix:
                result.append(prefix)
        else:
            arrange(number - 1, '()' + prefix)
            arrange(number - 1, prefix + '()')
            arrange(number - 1, '(' + prefix + ')')
            arrange(number - 1, prefix + prefix)

    arrange(n, '')
    result.sort()
    return result

    #     return '(())', '()()'
    # elif n == 3:
    #     return '((()))', '(()())', '(())()', '()(())', '()()()'
    # elif n == 4:
    #     return '(((())))',
    #            '((()()))', '((())())', '((()))()',
    #            '(()(()))', '(())(())', '(())()()', '(()())()'
    #            '()((()))', '()(()())', '()()(())',
    #            '()()()()'


if __name__ == '__main__':
    print(*get_parenthesis(int(input())), sep='\n')
